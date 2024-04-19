function Statement() {
  return (
    <div className="mt-3 me-3" style={{ fontSize: 14, color: "GrayText" }}>
      <p className="text-decoration-none">
        We respect your privary. Hence the above information will only be held
        securely on Chrome's&nbsp;
        <a href="https://developer.chrome.com/docs/extensions/reference/storage/#storage-areas">
          {`Session `}
        </a>
        until the browser is closed.
      </p>
    </div>
  );
}

export default Statement;
