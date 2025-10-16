import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from fuzzywuzzy import fuzz

nltk.download('punkt')
nltk.download('stopwords')

class BankingChatbot:
    def __init__(self, data_path='banking_data.json'):
        self.data_path = data_path
        self.load_data()
        self.index_questions()

    def load_data(self):
        with open(self.data_path) as file:
            self.data = json.load(file)

    def index_questions(self):
        stop_words = set(stopwords.words('english'))
        ps = PorterStemmer()

        self.indexed_questions = {
            self.preprocess(q['question'], ps, stop_words): q['answer']
            for q in self.data['questions']
        }

    @staticmethod
    def preprocess(text, ps, stop_words):
        words = word_tokenize(text)
        words = [ps.stem(word.lower()) for word in words if word.isalnum() and word.lower() not in stop_words]
        return ' '.join(words)

    def get_answer(self, user_input):
        processed_input = self.preprocess(user_input, PorterStemmer(), set(stopwords.words('english')))
        
        # Fuzzy matching to find the closest question
        best_match = max(self.indexed_questions.keys(), key=lambda question: fuzz.ratio(processed_input, question))
        
        # If the best match has a similarity score greater than a threshold, consider it
        if fuzz.ratio(processed_input, best_match) > 60:  # Adjust the threshold as needed
            return self.indexed_questions[best_match]
        else:
            return None

    def add_question(self, new_question, new_answer):
        self.data['questions'].append({"question": new_question, "answer": new_answer})
        self.indexed_questions[self.preprocess(new_question, PorterStemmer(), set(stopwords.words('english')))] = new_answer

        with open(self.data_path, 'w') as file:
            json.dump(self.data, file, indent=2)

    def run(self):
        while True:
            user_input = input("You: ").lower()
            if user_input == 'exit':
                break

            answer = self.get_answer(user_input)

            if answer:
                print("Chatbot:", answer)
            else:
                print("Chatbot: I don't know the answer. Can you teach me?")
                new_answer = input("You: ")
                self.add_question(user_input, new_answer)
                print("Chatbot: Thanks for teaching me!")

if __name__ == "__main__":
    chatbot = BankingChatbot()
    chatbot.run()
