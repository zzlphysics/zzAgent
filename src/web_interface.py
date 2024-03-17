# src/web_interface.py

from flask import Flask, request, jsonify
from src.agent import Agent

class WebInterface:
    def __init__(self, agent):
        self.agent = agent

    def start(self):
        # 这里应该是启动Web界面的逻辑
        pass
