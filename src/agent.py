from src.llm import LLM
class Agent:
    def __init__(self):
        self.llm = LLM()  # 初始化LLM实例
    def generate_response(self, user_input):
        # 目前，Agent只是简单地将用户输入传递给LLM
        # 在未来，这里可以添加更复杂的逻辑，例如调用其他工具或服务
        return self.llm.generate_response(user_input)
