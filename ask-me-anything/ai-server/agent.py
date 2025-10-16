import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import ChatOpenAI
from langchain.agents.load_tools import load_tools
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv(find_dotenv())

class Agent:
    def __init__(self, url):
        self.url = url
        self.setup_tools()

    def setup_tools(self):
        if self.url is not None:
            loader = WebBaseLoader(self.url)
            docs = loader.load()
            documents = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200
            ).split_documents(docs)
            vector = FAISS.from_documents(documents, OpenAIEmbeddings())
            retriever = vector.as_retriever()
            retriever_tool = create_retriever_tool(retriever, "websearch_retriever", "Search the web for answers")
            self.llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
            self.tools = [retriever_tool]
            prompt = ChatPromptTemplate.from_messages(
                [("system", 
                """
                You are very knowledgeable and intelligent person. 
                You have given a big knowledgebase. 
                Based on the user's question provide answers from the knowledgebase. 
                If you don't know the answer, you can ask the user for more information. 
                Or else take a look into web. While answering provide the source of the information.
                Do not fake the information. Provide the correct information.

                Try to provide answer from the websearch_retriever tool before using other tools. 
                If you didn't find the answer, then find the meta data from the websearch_retriever tool.
                And then try to search those meta data in other tools. And then provide the answer.
                """
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}")]
            )
            self.agent = create_tool_calling_agent(self.llm, self.tools, prompt)
            self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)
            self.message_history = ChatMessageHistory()

    def get_response(self, input_message):
        agent_with_chat_history = RunnableWithMessageHistory(
            self.agent_executor,
            lambda session_id: self.message_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )
        response = agent_with_chat_history.invoke(
            {"input": input_message},
            config={"configurable": {"session_id": self.url}},
        )
        return response["output"]
