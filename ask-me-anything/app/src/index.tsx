import ReactDOM from "react-dom/client";
import { App, EntryPage, ErrorPage, LoadPage } from "./App";
import "./index.css";

const msg = {
  from: "popup",
  to: "background",
};

const root = ReactDOM.createRoot(document.getElementById("popup")!);

chrome.runtime.sendMessage(msg);

chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.from === "background") {
    if (message.url === undefined || message.url === "") {
      root.render(<ErrorPage />);
    } else {
      if (message.name === "" || message.name === undefined) {
        root.render(<EntryPage />);
      } else {
        root.render(<App message={message} />);
      }
    }
  }
});

root.render(<LoadPage />);
