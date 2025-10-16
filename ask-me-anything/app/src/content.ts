const msg = {
  from: "content",
  to: "background",
  url: window.location.href,
};

// send to background.ts
chrome.runtime.sendMessage(msg);

export {};
