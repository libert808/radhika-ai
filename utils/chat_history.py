import json
import os
from datetime import datetime
from typing import List, Dict

class ChatHistory:
    def __init__(self, history_file: str = "data/chat_history.json"):
        self.history_file = history_file
        self.ensure_data_directory()
        self.history = self.load_history()

    def ensure_data_directory(self):
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)

    def load_history(self) -> List[Dict]:
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def add_message(self, role: str, content: str):
        message = {
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        }
        self.history.append(message)
        self.save_history()

    def save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)

    def clear_history(self):
        self.history = []
        self.save_history()

    def get_recent_messages(self, limit: int = 10) -> List[Dict]:
        return self.history[-limit:]
