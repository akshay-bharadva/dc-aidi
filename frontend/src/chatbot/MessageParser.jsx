import React from "react";
import axios from 'axios';
import { createClientMessage, createChatBotMessage } from 'react-chatbot-kit';

const MessageParser = ({ children, actions }) => {
  const parse = async (message) => {
    console.log(message);

    if(message !== ""){

      const apiEndpoint = 'http://localhost:5000/chatbot';
      const headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin':"*"
      };
  
      const data = {
        user_input: message,
      };
  
  try {
        const response = await axios.post(apiEndpoint, data, { headers });
        console.log("response",response)
        // const message = createClientMessage(response.data.response);
        actions.handleBotResponse(response.data.response);

        return response.data.response;
      } catch (error) {
        console.error('Error communicating with the API:', error.message);
        return '';
      }
    
    }

  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          parse: parse,
          actions: {},
        });
      })}
    </div>
  );
};

export default MessageParser;
