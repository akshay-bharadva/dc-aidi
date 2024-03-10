import streamlit as st
from langchain_community.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
import os

retriever = None

def ingest_document(uploaded_file):
    # Load document if file is uploaded
    if uploaded_file is not None:
        documents = [uploaded_file.read().decode()]
    # Split documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.create_documents(documents)
    # Select embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
    # Create a vectorstore from documents
    db = Chroma.from_documents(texts, embeddings)
    # Create retriever interface
    global retriever
    retriever = db.as_retriever()
    return retriever

def generate_response(query_text):
    # Create QA chain
    openai_api_key=os.environ['OPENAI_API_KEY']
    print(openai_api_key)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=openai_api_key), chain_type='stuff', retriever=retriever, )
    return qa.run(query_text)


st.set_page_config(page_title='🤖 Ask the Doc App')
st.subheader('LLM + RAG - Ask the Doc App')
with st.sidebar:
    with st.form('myform', clear_on_submit=False):    
        openai_api_key = st.text_input('OpenAI API Key', type='password')
        uploaded_file = st.file_uploader('Upload an article', type='txt')
        submitted = st.form_submit_button('Ingest')
        if openai_api_key and openai_api_key.startswith('sk-') and uploaded_file:
            os.environ['OPENAI_API_KEY'] = openai_api_key
            with st.spinner('Ingesting the file...'):
                result = ingest_document(uploaded_file)
                if result:
                    st.success('File ingested successfully!')


st.title('🤖 Ask the Doc App')

# chat
if not retriever:
    st.write(f'Add OpenAI Secret Key and upload file to chat.')

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?", disabled=not retriever):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = generate_response(prompt)
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})