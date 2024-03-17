import docker
from docker.models.containers import Container
class DockerIntegration:
    def __init__(self, tool_manager, docker_host):
        self.docker_client = docker.DockerClient(base_url=docker_host)
        self.tool_manager = tool_manager
    def run_container(self, image, command):
        """启动一个新的Docker容器并执行命令"""
        container = self.docker_client.containers.run(image, command, detach=True)
        return container
    def get_container_logs(self, container):
        """获取容器的日志"""
        if isinstance(container, Container):
            return container.logs()
        return None