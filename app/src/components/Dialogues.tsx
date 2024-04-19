import Question from "./Question";
import Response from "./Response";

interface IDialogues {
  message: any,
  dialogues: {
    question: string;
    response: string;
  }[];
  showHistory: boolean;
  collapsed: boolean;
}

function Dialogues({ message, dialogues, showHistory, collapsed }: IDialogues) {
  const expandedStyle = {
    width: "100%",
    maxHeight: "400px",
    minHeight: "40px",
    height: "400px",
    overflow: "hidden",
  };
  return (
    <div style={expandedStyle}>
      <div
        style={{
          overflowY: "scroll",
          width: "100%",
          height: "100%",
          paddingRight: "17px",
          boxSizing: "content-box",
        }}
      >
        <Response response={`Hi ${message?.name ? message?.name : 'there'}! How can I help you?`} />
        {!collapsed &&
          showHistory &&
          dialogues.map((dialogue, i) => (
            <div>
              <Question question={dialogue.question} />
              <Response response={dialogue.response} />
            </div>
          ))}
        {!collapsed && !showHistory && dialogues.length > 0 && (
          <div>
            <Question question={dialogues[dialogues.length - 1].question} />
            <Response response={dialogues[dialogues.length - 1].response} />
          </div>
        )}
      </div>
    </div>
  );
}

export default Dialogues;
