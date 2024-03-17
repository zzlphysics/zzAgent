import docker

try:
    client = docker.from_env()
    print(client.version())
except Exception as e:
    print(f"Error connecting to Docker: {e}")
