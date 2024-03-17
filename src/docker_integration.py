import docker
from docker.models.containers import Container

class DockerIntegration:
    def __init__(self, tool_manager, docker_host=None):
        # 如果 docker_host 为 None，DockerClient 会使用默认的 Unix 套接字路径
        self.docker_client = docker.DockerClient(base_url=docker_host if docker_host else None)
        self.tool_manager = tool_manager

    def run_container(self, image, command):
        container = self.docker_client.containers.run(image, command, detach=True)
        return container

    def get_container_logs(self, container):
        if isinstance(container, Container):
            return container.logs()
        return None
