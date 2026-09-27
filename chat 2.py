def get_response(user_input, name):
    user_input = user_input.lower().strip()
    
    # Predefined replies and conversation paths
    if "hello" in user_input or "hi" in user_input:
        return f"Hi {name}! It's great to talk to you. What's on your mind today?"
    elif "how are you" in user_input:
        return f"I'm functioning perfectly, thanks for asking, {name}! How are you doing?"
    elif "good" in user_input or "fine" in user_input:
        return f"I'm glad to hear that, {name}! 😊"
    elif "bad" in user_input or "sad" in user_input:
        return f"I'm sorry to hear that, {name}. I hope your day gets better!"
    elif "your name" in user_input:
        return "I'm your custom Python chatbot! You haven't given me a specific name yet."
    elif "bye" in user_input:
        return f"Goodbye, {name}! Have a wonderful day!"
    else:
        return f"I see! Tell me more about that, {name}, or try asking 'how are you'!"

def chatbot():
    print("Chatbot: Hello! I'm your new AI assistant.")
    
    # User assigns their name to make it personalized
    user_name = input("Chatbot: What is your name? \nYou: ").strip()
    if not user_name:
        user_name = "Friend"
        
    print(f"\nChatbot: Awesome! Nice to meet you, {user_name}. Let's chat! (Type 'bye' to exit)")
    
    # Main conversational loop
    while True:
        user_message = input(f"\n{user_name}: ")
        
        bot_reply = get_response(user_message, user_name)
        print(f"Chatbot: {bot_reply}")
        
        if "bye" in user_message.lower():
            break

if __name__ == "__main__":
    chatbot()
