import { Paper } from "@mui/material";

interface IQuestion {
  question: string;
}
function Question({ question }: IQuestion) {
  return (
    <div className="d-flex justify-content-end mb-2">
      <div className="d-flex">
        <div className="" style={{ maxWidth: "90%" }}>
          <Paper
            className="ps-2 pe-2 pt-1 pb-1 ms-2 me-2"
            elevation={0}
            style={{ textAlign: "left", background: "rgb(232 232 232)" }}
          >
            {question}
          </Paper>
        </div>
        <h3 className="">🧐</h3>
      </div>
    </div>
  );
}

export default Question;
