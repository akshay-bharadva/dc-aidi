import { Paper } from "@mui/material";
import { Dot } from "react-animated-dots";
import MarkdownPreview from "@uiw/react-markdown-preview";

interface IResponse {
  response: string;
}
function Response({ response }: IResponse) {
  return (
    <div className="d-flex mb-2">
      <h3>🤖</h3>
      <div style={{ maxWidth: "90%" }}>
        {response === "" ? (
          <span className="mt-0 mb-0" style={{ fontSize: "160%" }}>
            <Dot>.</Dot>
            <Dot>.</Dot>
            <Dot>.</Dot>
          </span>
        ) : (
          <Paper
            className="ps-2 pe-2 pt-1 pb-1 ms-2 me-2"
            elevation={0}
            style={{ textAlign: "left", background: "rgb(232 232 232)" }}
          >
            <MarkdownPreview
              source={response}
              style={{ background: "rgb(232 232 232)", color: "rgb(0,0,0)" }}
            />
          </Paper>
        )}
      </div>
    </div>
  );
}

export default Response;
