import os
import time
from dotenv import load_dotenv
from src.llm import LLM
from src.agent import Agent
from src.web_interface import WebInterface
from src.tool_manager import ToolManager
from src.docker_integration import DockerIntegration
from src.browser_integration import BrowserIntegration
from flask import Flask

# 加载当前目录下的.env文件
load_dotenv()

tool_manager = ToolManager()

docker_integration = DockerIntegration(tool_manager)
tool_manager.register_tool('docker', docker_integration)

browser_integration = BrowserIntegration()
tool_manager.register_tool('browser', browser_integration)

llm = LLM()  # 初始化LLM实例

agent = Agent(tool_manager, llm)
web_interface = WebInterface(agent)  # 将Flask app传递给WebInterface

# 阻塞主线程，防止它退出
try:
    while True:
        time.sleep(1)  # 主线程可以执行一些其他任务或简单地阻塞
except KeyboardInterrupt:
    # 如果有Ctrl+C中断，可以在这里添加清理代码
    pass