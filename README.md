# AI Girlfriend Chat

A beautiful terminal-based AI girlfriend chatbot that provides an interactive and emotionally aware conversation experience.

## Features

- 🎨 Beautiful terminal UI with rich formatting
- 💕 Emotionally aware responses
- 💬 Persistent chat history
- 🎭 Customizable character personality
- 🔧 Easy to extend and modify

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
Create a `.env` file with:
```
OPENROUTER_BASE_URL=your_base_url
OPENROUTER_API_KEY=your_api_key
```

3. Run the chatbot:
```bash
python main.py
```

## Commands

- `/clear` - Clear chat history and screen
- `/exit` - Exit the chat

## Customization

You can customize the AI girlfriend's personality by modifying:
- `config/character.json` - Character details and appearance
- `config/system_prompt.txt` - Personality and behavior guidelines

## Project Structure

- `main.py` - Main application entry point
- `config/` - Configuration files
  - `character.json` - Character settings
  - `system_prompt.txt` - AI behavior guidelines
- `utils/` - Utility modules
  - `ai_client.py` - AI API communication
  - `chat_history.py` - Chat history management
- `ui/` - User interface
  - `chat_window.py` - Terminal UI components
- `data/` - Generated data storage
  - `chat_history.json` - Saved chat history
