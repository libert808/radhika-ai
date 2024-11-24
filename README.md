# AI Anchoring Assistant 🎤

An intelligent, terminal-based AI assistant that helps you create professional anchorings and speeches with a beautiful, modern interface.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 🤖 **Intelligent AI Assistant**: Powered by advanced language models for high-quality content generation
- 🎨 **Beautiful UI**: Modern, pastel-themed terminal interface using Rich
- 📝 **Structured Output**: Well-organized XML-based content structure
- 💬 **Interactive**: Engaging conversation flow with clarifying questions
- 🔄 **Real-time Streaming**: See responses as they're generated
- 📊 **Comprehensive Output**: Includes metadata, content, and delivery notes

## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/anchoring_agent.git
cd anchoring_agent
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=your_base_url_here  # Optional
```

5. **Run the application**
```bash
python main.py
```

## 💡 Usage

1. **Start a New Anchoring**
   - Launch the application
   - Enter your topic or event details
   - Follow the AI's prompts for additional information

2. **Available Commands**
   - Type `exit` or `quit` to close the application
   - Type `clear` to reset the conversation

3. **Output Structure**
   The generated content includes:
   - **Metadata**: Title, audience, duration, and type
   - **Content**: Opening, main points, transitions, and closing
   - **Notes**: Delivery instructions, timing, and emphasis points

## 🏗️ Project Structure

```
anchoring_agent/
├── main.py           # Application entry point
├── ai_agent.py       # AI agent implementation
├── ui.py            # Terminal UI implementation
├── config.py        # Configuration and system prompt
└── requirements.txt # Project dependencies
```

## ⚙️ Configuration

The application can be customized through:
- `config.py`: Modify themes, system prompt, and model settings
- `.env`: Set API credentials and custom base URL

## 🎯 Use Cases

- 🎭 Event hosting and anchoring
- 🎤 Speech writing
- 📢 Presentations
- 🎉 Ceremony scripts
- 🤝 Welcome addresses

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Rich library for the beautiful terminal interface
- OpenAI for the powerful language models
- All contributors and users of this project
