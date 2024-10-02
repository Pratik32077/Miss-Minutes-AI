import random

class Karen:
    def __init__(self):
        self.responses = {
            "hello": ["Hello!", "Hi there!", "Hey, how can I help you?"],
            "goodbye": ["Goodbye!", "See you later!", "Take care!"],
            "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
            "default": ["I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure what you mean."]
        }

    def respond(self, query):
        query = query.lower()
        if "hello" in query:
            return random.choice(self.responses["hello"])
        elif "bye" in query or "goodbye" in query:
            return random.choice(self.responses["goodbye"])
        elif "thanks" in query or "thank you" in query:
            return random.choice(self.responses["thanks"])
        else:
            return random.choice(self.responses["default"])

if __name__ == "__main__":
    karen = Karen()
    print("Karen: Hi! I'm Karen, your personal AI assistant. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Karen: Goodbye!")
            break
        response = karen.respond(user_input)
        print("Karen:", response)
