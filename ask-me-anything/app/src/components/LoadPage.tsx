import { Dot } from "react-animated-dots";

const LoadPage: React.FC = () => {
  return (
    <div>
      <header></header>
      <body className="ps-3 pt-3">
        <div
          style={{
            position: "fixed",
            left: "50%",
            top: "50%",
            transform: "translate(-50%, -50%)",
          }}
        >
          <span className="mt-0 mb-0" style={{ fontSize: "160%" }}>
            <Dot>🤖</Dot>
            <Dot>🤖</Dot>
            <Dot>🤖</Dot>
          </span>
          <br />
          Loading...
        </div>
      </body>
    </div>
  );
};

export default LoadPage;
