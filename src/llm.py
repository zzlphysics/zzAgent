import openai
import os

class LLM:
    def __init__(self):
        # 从环境变量中读取OpenAI的API密钥
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.base_url = os.getenv('OPENAI_API_BASE')
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        self.client = openai.OpenAI(api_key=self.api_key, base_url=self.base_url)

    def generate_response(self, prompt):
        try:
            completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
            )
            return(completion.choices[0].message)
        except Exception as e:
            print(f"Error in generating response from OpenAI: {e}")
            return "Unable to generate response due to an error."
