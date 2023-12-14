import { createChatBotMessage } from "react-chatbot-kit";

const config = {
  initialMessages: [createChatBotMessage(`Hello! I'm Hoot, your personal baking assistance. How may I help you?`)],
  botName: "Hoot",
  customStyles: {
    botMessageBox: {},
    chatButton: {},
  },
};

export default config;
