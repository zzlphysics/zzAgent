import os
import threading
from src.agent import Agent
from src.web_interface import WebInterface
from src.tool_manager import ToolManager
from src.docker_integration import DockerIntegration
from src.browser_integration import BrowserIntegration
from flask import Flask

app = Flask(__name__)

# 初始化工具管理器
tool_manager = ToolManager()

# 集成Docker
docker_integration = DockerIntegration(tool_manager, os.getenv('DOCKER_HOST'))
tool_manager.register_tool('docker', docker_integration)

# 集成浏览器
browser_integration = BrowserIntegration()
tool_manager.register_tool('browser', browser_integration)

# 初始化Agent
agent = Agent(tool_manager)

# 启动Web接口
web_interface = WebInterface(agent)

def run_flask():
    # 启动Flask应用
    app.run(host='0.0.0.0', port=5000)

# 在单独的线程中运行Flask应用
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# 在此之后可以执行后续的操作

if __name__ == "__main__":
    # 这里不需要额外的main函数定义，因为if __name__ == "__main__":块本身就是程序的入口点
    pass
