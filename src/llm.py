import requests
import os
class LLM:
    def __init__(self):
        # 初始化智谱AI API的URL和API密钥
        self.api_url = 'https://api.zhipu.ai/v1/completions'
        self.api_key = os.getenv('ZHIPU_AI_API_KEY')
    def generate_response(self, prompt):
        # 使用智谱AI API生成响应
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
        response.raise_for_status()  # 如果响应包含错误，抛出异常
        choices = response.json()['choices']
        if choices:
            return choices[0]['text'].strip()
        else:
            return "抱歉，我没有理解您的问题。"