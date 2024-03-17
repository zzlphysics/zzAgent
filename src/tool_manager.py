class ToolManager:
    def __init__(self):
        self.tools = {}  # 存储注册的工具，键为工具名称，值为工具实例
    def register_tool(self, tool_name, tool_instance):
        """注册一个工具到工具管理器中"""
        self.tools[tool_name] = tool_instance
    def get_tool(self, tool_name):
        """从工具管理器中获取一个工具"""
        return self.tools.get(tool_name, None)