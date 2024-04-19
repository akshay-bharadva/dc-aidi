let msg = {
  from: "background",
  to: "popup",
  url: "",
  name: "",
};

// event listeners and handlers
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.from === "content") {
    msg.url = message.url;
  }
  if (message.from === "popup") {
    chrome.storage.session.get(["name"]).then((result) => {
      msg.name = result.name;
      chrome.runtime.sendMessage(msg);
    });
  }
});

export {};
