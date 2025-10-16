const url = window.location.href;

const msg = {
  from: "injected",
  to: "content",
  url: url,
};

window.postMessage(msg);

export {};
