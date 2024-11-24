import json
import os
import shutil
import re
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.panel import Panel

class ChatWindow:
    def __init__(self, character_config_path="config/character.json"):
        # Create custom theme with pastel colors
        custom_theme = Theme({
            'welcome': 'rgb(147,112,219)',      # Soft purple
            'user': 'rgb(255,182,193)',         # Light pink
            'assistant': 'rgb(173,216,230)',    # Light blue
            'header': 'rgb(144,238,144)',       # Light green
            'command': 'rgb(255,218,185)',      # Peach
            'border': 'rgb(176,196,222)',       # Light steel blue
            'emotion': 'rgb(221,160,221)',      # Plum
            'mood': 'rgb(255,182,193)',         # Soft pink
            'style': 'rgb(176,224,230)',        # Powder blue
            'action': 'rgb(255,218,185)',       # Peach
            'emojis': 'rgb(255,192,203)'        # Pink
        })
        self.console = Console(theme=custom_theme)
        self.load_character_config(character_config_path)
        self.terminal_width = shutil.get_terminal_size().columns
        self.messages = []

    def load_character_config(self, config_path):
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        except:
            self.config = {
                "name": "Radhika",
                "emoji": "👩‍🎨",
                "user_emoji": "👤"
            }

    def _extract_xml_tags(self, content):
        tags = {
            'mood': None,
            'emotion': None,
            'style': None,
            'text': None,
            'action': None,
            'emojis': None
        }
        
        # Extract each tag content using regex
        for tag in tags.keys():
            pattern = f"<{tag}>(.*?)</{tag}>"
            match = re.search(pattern, content, re.DOTALL)
            if match:
                tags[tag] = match.group(1).strip()
        
        # If there's no text tag, treat the whole content as text
        if not tags['text'] and not any(f"<{tag}>" in content for tag in tags.keys()):
            tags['text'] = content
        
        return tags

    def _format_message(self, content, is_user=False):
        if is_user:
            return self._format_user_message(content)
        return self._format_assistant_message(content)

    def _format_user_message(self, content):
        name = "You"
        emoji = self.config["user_emoji"]
        header = f"{name} {emoji}"
        
        # Format user message simply
        lines = content.split('\n')
        formatted_lines = []
        for line in lines:
            while len(line) > self.terminal_width - 3:
                split_point = line[:self.terminal_width - 3].rfind(' ')
                if split_point == -1:
                    split_point = self.terminal_width - 3
                formatted_lines.append(line[:split_point])
                line = line[split_point:].lstrip()
            if line:
                formatted_lines.append(line)

        return [
            header,
            "─" * len(header),
            *[f" {line}" for line in formatted_lines]
        ]

    def _format_assistant_message(self, content):
        tags = self._extract_xml_tags(content)
        name = self.config["name"]
        emoji = self.config["emoji"]
        
        # Create rich header with all metadata
        header_parts = [f"{name} {emoji}"]
        if tags['mood']:
            header_parts.append(f"• [mood]{tags['mood']}[/]")
        if tags['emotion']:
            header_parts.append(f"• [emotion]{tags['emotion']}[/]")
        if tags['style']:
            header_parts.append(f"• [style]{tags['style']}[/]")
        
        header = " ".join(header_parts)
        
        # Format the main message text
        text_content = tags['text'] if tags['text'] else content
        lines = text_content.split('\n')
        formatted_lines = []
        for line in lines:
            while len(line) > self.terminal_width - 3:
                split_point = line[:self.terminal_width - 3].rfind(' ')
                if split_point == -1:
                    split_point = self.terminal_width - 3
                formatted_lines.append(line[:split_point])
                line = line[split_point:].lstrip()
            if line:
                formatted_lines.append(line)
        
        message = [
            header,
            "─" * len(header.replace('[/]', '').replace('[mood]', '').replace('[emotion]', '').replace('[style]', '')),
            *[f" {line}" for line in formatted_lines]
        ]
        
        # Add action if present
        if tags['action']:
            message.append(f" [action]* {tags['action']} *[/]")
        
        # Add emojis if present
        if tags['emojis']:
            message.append(f" [emojis]{tags['emojis']}[/]")
        
        return message

    def display_welcome(self):
        width = self.terminal_width
        self.console.print("╭" + "─" * (width - 2) + "╮", style="border")
        self.console.print("│" + " " * (width - 2) + "│", style="border")
        
        title = "✨ Welcome to AI Chat ✨"
        padding = (width - len(title) - 2) // 2
        self.console.print("│" + " " * padding + title + " " * (width - len(title) - padding - 2) + "│", style="welcome")
        
        subtitle = f"Chatting with {self.config['name']} {self.config['emoji']}"
        padding = (width - len(subtitle) - 2) // 2
        self.console.print("│" + " " * padding + subtitle + " " * (width - len(subtitle) - padding - 2) + "│", style="assistant")
        
        self.console.print("│" + " " * (width - 2) + "│", style="border")
        self.console.print("│  Commands:" + " " * (width - 12) + "│", style="header")
        self.console.print("│    /clear - Clear chat history" + " " * (width - 29) + "│", style="command")
        self.console.print("│    /exit  - Exit chat" + " " * (width - 22) + "│", style="command")
        
        self.console.print("│" + " " * (width - 2) + "│", style="border")
        self.console.print("╰" + "─" * (width - 2) + "╯", style="border")
        self.console.print()

    def update_chat(self, messages):
        self.messages = messages
        self.display_messages()

    def display_messages(self):
        os.system('clear')
        self.display_welcome()
        
        for msg in self.messages:
            is_user = msg['role'] == 'user'
            lines = self._format_message(msg['content'], is_user)
            
            # Print each line with appropriate style
            style = "user" if is_user else "assistant"
            for line in lines:
                self.console.print(Text.from_markup(line), style=style)
            self.console.print()  # Single line spacing between messages

    def clear_screen(self):
        os.system('clear')
        self.messages = []
        self.display_welcome()

    def get_input(self):
        return self.console.input("[user]> [/]")
