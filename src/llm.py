import requests
import os

class LLM:
    def __init__(self):
        self.api_url = 'https://api.zhipu.ai/v1/completions'
        self.api_key = os.getenv('ZHIPU_AI_API_KEY')
        if not self.api_key:
            raise ValueError("ZHIPU_AI_API_KEY environment variable not set.")

    def generate_response(self, prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'prompt': prompt,
            'max_tokens': 100,
            'n': 1,
            'stop': None,
            'temperature': 0.5,
        }
        response = requests.post(self.api_url, json=data, headers=headers)
        response.raise_for_status()
        choices = response.json()['choices']
        if choices:
            return choices[0]['text'].strip()
        else:
            return "抱歉，我没有理解您的问题。"
