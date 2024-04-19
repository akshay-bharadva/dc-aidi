import { useState } from "react";
import { IconButton, InputAdornment, TextField } from "@mui/material";
import { CircularProgress } from "@mui/material";
import InputLabel from "@mui/material/InputLabel";
import CheckIcon from "@mui/icons-material/Check";
import Statement from "./Statement";

const EntryPage: React.FC = () => {
  const submitName = () => {
    chrome.storage.session.set({ name: name }).then(() => {
      const msg = {
        from: "popup",
        to: "background",
      };
      chrome.runtime.sendMessage(msg);
    });
  };

  const [name, setName] = useState("");
  const [saving, setSaving] = useState(false);

  return (
    <div>
      <header></header>
      <body className="ps-3 pt-3">
        <div className="mt-3 mb-2">
          <div className="mt-3 me-3" style={{ fontSize: 18 }}>
            <h3>Ask me Anything</h3>
            <p className="text-decoration-none">
              Welcome to the QueryGenius!
              <br/>
              Please enter your name to begin.
            </p>
          </div>
          <TextField
            id="name_input"
            onChange={(e) => setName(e.target.value)}
            variant="standard"
            label="Enter Your Name"
            style={{ width: "90%" }}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    aria-label="ask question"
                    onClick={submitName}
                    edge="end"
                  >
                    {!saving ? (
                      <CheckIcon
                        color="action"
                        onClick={() => setSaving(true)}
                      />
                    ) : (
                      <CircularProgress size={20} />
                    )}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
          <Statement />
        </div>
      </body>
    </div>
  );
};
export default EntryPage;
