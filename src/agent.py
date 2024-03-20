class Agent:
    def __init__(self, tool_manager, llm):
        self.tool_manager = tool_manager
        self.llm = llm

    def handle_request(self, request):
        """
        处理来自用户或系统的请求。
        - 分析请求内容
        - 决定使用哪个工具或服务来处理请求
        - 调用相应的工具或服务并返回结果
        """
        # 使用LLM来理解请求内容和决定如何处理
        response = self.llm.generate_response(request)

        # 基于LLM的响应，决定调用哪个工具
        if "使用Docker" in response:
            docker_tool = self.tool_manager.get_tool('docker')
            result = docker_tool.run_container(image="hello-world", command="")
            return f"Docker工具已执行，结果：{result}"
        elif "查询信息" in response:
            browser_tool = self.tool_manager.get_tool('browser')
            browser_tool.visit_url("https://www.bing.com")
            title = browser_tool.get_title()
            return f"浏览器工具已访问网页，页面标题：{title}"
        else:
            return f"response: {response}"

    def create_new_tool(self, tool_name):
        """
        根据需要创建新工具。这是一个概念性的函数示例，
        实际创建工具的逻辑将取决于具体需求和工具的复杂性。
        """
        # 伪代码，实际实现将依赖于具体需求
        if tool_name not in self.tool_manager.tools:
            # 创建工具的逻辑
            print(f"创建新工具：{tool_name}")
        else:
            print(f"工具{tool_name}已存在。")
