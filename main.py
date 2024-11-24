import os
from utils.chat_history import ChatHistory
from utils.ai_client import AIClient
from ui.chat_window import ChatWindow

def load_system_prompt():
    with open("config/system_prompt.txt", "r") as f:
        return f.read()

def main():
    # Initialize components
    chat_history = ChatHistory()
    ai_client = AIClient()
    chat_window = ChatWindow()
    system_prompt = load_system_prompt()

    # Display initial screen
    chat_window.clear_screen()

    while True:
        # Get user input
        user_input = chat_window.get_input()

        # Handle commands
        if user_input.lower() == '/exit':
            break
        elif user_input.lower() == '/clear':
            chat_history.clear_history()
            chat_window.clear_screen()
            continue

        # Add user message to history
        chat_history.add_message('user', user_input)

        # Update display with user message
        messages = chat_history.get_recent_messages()
        chat_window.update_chat(messages)

        # Get AI response
        messages = [
            {'role': msg['role'], 'content': msg['content']}
            for msg in chat_history.get_recent_messages()
        ]
        
        response = ai_client.get_response(messages, system_prompt)
        
        # Add AI response to history
        chat_history.add_message('assistant', response['message'])
        
        # Update the messages list with the new response including emotion
        messages = chat_history.get_recent_messages()
        messages[-1]['emotion'] = response['emotion']

        # Update chat display
        chat_window.update_chat(messages)

if __name__ == "__main__":
    main()
