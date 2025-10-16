from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from agent import Agent

app = Flask(__name__)
cors = CORS(app)

@app.route('/api/v1/chat', methods=['POST'])
@cross_origin()
def chat():
  print(request.json)
  # Get the user's message from the request
  active_page = request.json['url']
  user_message = request.json['message']

  agent = Agent(url=active_page)
  agent_response = agent.get_response(user_message)

  # Return the agent's response to the client
  return jsonify({'response': agent_response})

if __name__ == '__main__':
  app.run(debug=True)