import random

# Predefined set of responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I help you with?", "Hey! What do you need assistance with?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "Happy to help!", "No problem!"],
    "hours": ["Our working hours are 9 AM to 9 PM, Monday to Saturday."],
    "location": ["We are located at 123 Main Street, YourCity."],
    "default": ["I'm sorry, I didn't quite get that. Could you please rephrase?"]
}

# Function to generate a response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return random.choice(responses["greeting"])
    elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
        return random.choice(responses["goodbye"])
    elif "thanks" in user_input or "thank you" in user_input:
        return random.choice(responses["thanks"])
    elif "hours" in user_input or "open" in user_input or "time" in user_input or "timings" in user_input:
        return random.choice(responses["hours"])
    elif "location" in user_input or "address" in user_input or "where" in user_input:
        return random.choice(responses["location"])
    else:
        return random.choice(responses["default"])

# Main chatbot function
def chatbot():
    print("StoreBot: Hello! Welcome to Our Store. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye" or user_input.lower() == "goodbye" or user_input.lower() == "exit":
            print("StoreBot:", random.choice(responses["goodbye"]))
            break
        else:
            response = get_response(user_input)
            print("StoreBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
