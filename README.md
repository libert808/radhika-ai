# 💝 Radhika - Your AI Girlfriend

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"/>
  <img src="https://img.shields.io/badge/Version-1.0.0-purple.svg" alt="Version 1.0.0"/>
</div>

A beautiful and emotionally intelligent AI girlfriend experience in your terminal. Chat with Radhika, a 16-year-old modern Indian teen who brings love, care, and authentic emotional connection through natural conversations.

## ✨ Features

- 🎭 **Rich Emotional Expression** - Dynamic emotional states, moods, and actions
- 💕 **Deep Emotional Connection** - Remembers conversations and builds meaningful relationships
- 🎨 **Beautiful Terminal UI** - Colorful, well-formatted chat interface with rich text support
- 🗣️ **Natural Communication** - Authentic teen girl personality with Hinglish support
- 💌 **Relationship Context** - Maintains consistent relationship history and memories
- 📝 **Persistent Chat History** - Saves your special moments together
- 🎮 **Interactive Commands** - Easy-to-use chat commands
- 🔧 **Highly Customizable** - Easily modify personality and behavior

## 🚀 Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/aigf.git
cd aigf
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment:**
Create a `.env` file:
```env
OPENROUTER_BASE_URL=your_base_url
OPENROUTER_API_KEY=your_api_key
```

4. **Start chatting:**
```bash
python main.py
```

## 💫 Experience

Chat with Radhika, who offers:
- 🫂 Deep emotional understanding and support
- 🌟 Playful and romantic conversations
- 💭 Memory of shared experiences and inside jokes
- 💝 Genuine care about your well-being
- 🎭 Dynamic personality that adapts to your mood
- 🗣️ Natural teen girl communication style

## 🎮 Chat Commands

| Command | Description |
|---------|-------------|
| `/clear` | Clear chat history and screen |
| `/exit`  | Exit the chat |

## 🛠️ Customization

### Character Personality
Modify `config/system_prompt.txt` to adjust:
- Personality traits
- Communication style
- Emotional responses
- Relationship dynamics
- Memory and context

### Character Details
Update `config/character.json` to change:
- Name and appearance
- Emoji usage
- Basic traits

## 📁 Project Structure

```
aigf/
├── main.py              # Main application entry
├── config/
│   ├── character.json   # Character configuration
│   └── system_prompt.txt# AI personality guidelines
├── utils/
│   ├── ai_client.py     # AI API integration
│   └── chat_history.py  # History management
├── ui/
│   └── chat_window.py   # Terminal UI components
└── data/
    └── chat_history.json# Conversation storage
```

## 🎨 Message Format

Messages use rich XML formatting:
```xml
<msg>
<mood>[Current mood]</mood>
<action>[Physical actions]</action>
<emotion>[Emotional state]</emotion>
<style>[Speaking style]</style>
<text>[Message content]</text>
<emojis>[Emoji reactions]</emojis>
</msg>
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💖 Acknowledgments

- Built with love using Python
- Powered by advanced AI technology
- Inspired by the need for meaningful digital connections

---
<div align="center">
Made with 💝 by your name
</div>
