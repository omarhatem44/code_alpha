import nltk
import random
import string
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

responses = {
    "greetings": ["Hello!", "Hi there!", "Greetings!", "How can I assist you today?"],
    "goodbye": ["Goodbye!", "Take care!", "See you soon!", "Bye!"],
    "default": ["I'm sorry, I don't quite understand.", "Can you please rephrase that?", "Let's talk about something else."],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"]
}


def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hi", "hello", "hey", "greetings"]:
        return random.choice(responses["greetings"])
    elif user_input in ["bye", "goodbye", "see you", "later"]:
        return random.choice(responses["goodbye"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    else:
        return generate_response(user_input)

def generate_response(user_input):
    word_tokens = word_tokenize(user_input)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    filtered_tokens = [lemmatizer.lemmatize(w.lower()) for w in word_tokens if w not in stop_words]
    
    if "weather" in filtered_tokens:
        return "It's always sunny in the virtual world!"
    
    elif "name" in filtered_tokens:
        return "My name is ChatBot!"
    
    elif "love" in filtered_tokens:
        return "Love is a beautiful thing!"
    
    else:
        return random.choice(responses["default"])

def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("ChatBot:", random.choice(responses["goodbye"]))
            break
        
        else:
            response = chatbot_response(user_input)
            print("ChatBot:", response)

chatbot()
