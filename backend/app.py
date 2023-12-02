import sqlite3
from flask import Flask, request, jsonify, g
from datetime import datetime
from banking_chatbot import BankingChatbot

app = Flask(__name__)
chatbot = BankingChatbot()

# Connect to SQLite database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('chatbot_logs.db')
    return db

# Close database connection at the end of each request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            script_content = f.read()
            print(script_content)  # Add this line to print the content
            db.cursor().executescript(script_content)
        db.commit()

# Initialize the database when the app starts
init_db()

def log_interaction(user_input, bot_response, user_ip):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO chat_logs (user_input, bot_response, user_ip)
        VALUES (?, ?, ?)
    ''', (user_input, bot_response, user_ip))
    db.commit()

@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    data = request.json
    user_input = data.get('user_input', '')
    user_ip = request.remote_addr  # Get user's IP address
    
    # Get chatbot response
    answer = chatbot.get_answer(user_input)
    
    # Log the interaction
    log_interaction(user_input, answer, user_ip)
    
    if answer:
        response = {"response": answer}
    else:
        response = {"response": "I don't know the answer. Can you teach me?"}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    


# from flask import Flask, request, jsonify
# from banking_chatbot import BankingChatbot  # Import the BankingChatbot class from your chatbot module

# app = Flask(__name__)
# chatbot = BankingChatbot()  # Initialize your chatbot

# @app.route('/chatbot', methods=['POST'])
# def chatbot_endpoint():
#     data = request.json
#     user_input = data.get('user_input', '')
    
#     # Get chatbot response
#     answer = chatbot.get_answer(user_input)
    
#     if answer:
#         response = {"response": answer}
#     else:
#         response = {"response": "I am not sure what you are asking about."}
    
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)




