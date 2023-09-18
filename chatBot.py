import re

def simple_chatbot(user_input):
    # Define patterns and responses
    patterns = {
        r'hello.*|hi.*': "Hello! How can I assist you?",
        r'how are you.*': "I'm just a chatbot, but I'm here to help!",
        r'what.*your name.*': "I'm a chatbot, so I don't have a name.",
        r'bye|goodbye|see you': "Goodbye! Have a great day!",
        r'\b(?:thank you|thanks)\b': "You're welcome!",
        r'.*': "I'm sorry, I didn't quite understand that.",
    }
    
    # Search for a pattern match in the user input
    response = None
    for pattern, reply in patterns.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            response = reply
            break
    
    return response

def main():
    print("Chatbot: Hello! How can I assist you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = simple_chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
