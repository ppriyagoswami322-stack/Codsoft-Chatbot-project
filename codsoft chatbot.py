# Simple Chatbot Project in Python

# chatbot function
def chatbot():
    while True:
        user_input = input("You: "). lower()

        if "hello" in user_input:
            print("Bot: Nice to meet you!")
        elif "how are you" in user_input:
            print("Bot: I am fine! How can I help you?")
        elif "help" in user_input:
            print("Bot: I can help you. Try saying hello.")
        elif "bye" in user_input:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that")

    chatbot()          


        