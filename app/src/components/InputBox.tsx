import { IconButton, InputAdornment, TextField } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";

interface IInputBoxType {
  query: string;
  setQuery: (query: string) => void;
  submitQuery: () => void;
}
function InputBox({ query, setQuery, submitQuery }: IInputBoxType) {
  const handleKeyDown = (key: string) => {
    if (key === "Enter") {
      submitQuery();
    }
  };

  return (
    <TextField
      className="mt-1 mb-2"
      value={query}
      onChange={(e: any) => setQuery(e.target.value)}
      onKeyDown={(e: any) => handleKeyDown(e.key)}
      style={{ width: "98%", boxShadow: "10px" }}
      size="small"
      InputProps={{
        endAdornment: (
          <InputAdornment position="end">
            <IconButton
              aria-label="ask question"
              onClick={submitQuery}
              edge="end"
            >
              <SendIcon />
            </IconButton>
          </InputAdornment>
        ),
      }}
    />
  );
}

export default InputBox;
