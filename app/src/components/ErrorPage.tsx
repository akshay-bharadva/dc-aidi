const ErrorPage: React.FC = () => {
  return (
    <div>
      <header></header>
      <body className="ps-3 pt-3">
        <div
          style={{
            position: "fixed",
            left: "50%",
            top: "50%",
            transform: "translate(-50%,-50%)",
          }}
        >
          Please refresh current page
        </div>
      </body>
    </div>
  );
};

export default ErrorPage;
