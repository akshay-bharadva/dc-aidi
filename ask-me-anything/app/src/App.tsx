import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import axios from "axios";
import "./App.css";
import InputBox from "./components/InputBox";
import Dialogues from "./components/Dialogues";
import EntryPage from "./components/EntryPage";
import LoadPage from "./components/LoadPage";
import ErrorPage from "./components/ErrorPage";
import { API_ENDPOINT } from "./config";

interface IAppProps {
  message: any;
}
const App: React.FC<IAppProps> = ({ message }: IAppProps) => {
  async function fetchData() {
    if (!query) return;
    let newDialogue = {
      question: query,
      response: "",
    };
    try {
      const data = {
        name: message.name,
        url: message.url,
        message: query,
      };
      setQuery("");
      setDialogues([...dialogues, newDialogue]);
      const response = await axios.post(`${API_ENDPOINT}/api/v1/chat`, data);
      newDialogue.response = response.data.response;
      setDialogues([...dialogues, newDialogue]);
      // Process the response data here
      console.log(response.data);
    } catch (error) {
      // Handle any errors that occur during the request
      newDialogue.response = `I'm sorry there has been an error: ${error}`;
      setDialogues([...dialogues, newDialogue]);
      console.error(error);
    }
  }
  const [query, setQuery] = useState("");
  const [dialogues, setDialogues] = useState<
    { question: string; response: string }[] | never[]
  >([]);
  const [showHistory, setShowHistory] = useState(true);
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div>
      <body className="ps-3 pt-3 pe-3">
        <div>
          <Dialogues
            dialogues={dialogues}
            showHistory={showHistory}
            collapsed={collapsed}
            message={message}
          />
          <InputBox query={query} setQuery={setQuery} submitQuery={fetchData} />
        </div>
      </body>
    </div>
  );
};

export { App, LoadPage, ErrorPage, EntryPage };
