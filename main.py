import os
import threading
from src.agent import Agent
from src.web_interface import WebInterface
from src.tool_manager import ToolManager
from src.docker_integration import DockerIntegration
from src.browser_integration import BrowserIntegration
from flask import Flask

app = Flask(__name__)

tool_manager = ToolManager()

docker_integration = DockerIntegration(tool_manager)  # 移除了对 DOCKER_HOST 的引用
tool_manager.register_tool('docker', docker_integration)

browser_integration = BrowserIntegration()
tool_manager.register_tool('browser', browser_integration)

agent = Agent(tool_manager)
web_interface = WebInterface(app, agent)  # 将Flask app传递给WebInterface

def run_flask():
    app.run(host='0.0.0.0', port=5000)

flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()
