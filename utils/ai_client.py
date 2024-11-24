import os
from openai import OpenAI
import xml.etree.ElementTree as ET
from typing import Dict, Optional

class AIClient:
    def __init__(self):
        base_url = os.getenv('OPENROUTER_BASE_URL')
        api_key = os.getenv('OPENROUTER_API_KEY')
        
        if not base_url or not api_key:
            raise ValueError("Missing required environment variables: OPENROUTER_BASE_URL or OPENROUTER_API_KEY")
        
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = "anthropic/claude-3.5-haiku-20241022:beta"

    def get_response(self, messages: list, system_prompt: str) -> Dict[str, str]:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *messages
                ]
            )
            
            content = response.choices[0].message.content
            return self._parse_response(content)
            
        except Exception as e:
            return {
                "emotion": "concerned",
                "message": f"I'm having trouble responding right now. Could you please try again?"
            }

    def _parse_response(self, content: str) -> Dict[str, str]:
        try:
            # Clean up the content by removing extra whitespace and newlines
            content = ' '.join(line.strip() for line in content.split('\n'))
            
            # Extract emotion using simple string operations
            emotion_start = content.find('<emotion>') + len('<emotion>')
            emotion_end = content.find('</emotion>')
            emotion = content[emotion_start:emotion_end].strip() if emotion_start > -1 and emotion_end > -1 else "normal"
            
            # Extract message content
            msg_start = content.find('</emotion>') + len('</emotion>')
            msg_end = content.find('</msg>')
            message = content[msg_start:msg_end].strip() if msg_start > -1 and msg_end > -1 else content
            
            # Split message on <split> tags and join with newlines
            message = '\n'.join(part.strip() for part in message.split('<split>'))
            
            return {
                "emotion": emotion,
                "message": message
            }
        except Exception as e:
            return {
                "emotion": "normal",
                "message": content.strip()
            }
