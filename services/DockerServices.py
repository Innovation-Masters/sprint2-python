from abc import ABC, abstractmethod

class DockerServices(ABC):
    def __init__(self, porta, ip):
        self.porta = porta
        self.ip = ip

    def checkStatus(self):
        return f"IP e porta de conexão: {self.ip}:{self.porta}"

class ServiceBase(DockerServices):
    def __init__(self, porta, ip, graphUrl=None):
        super().__init__(porta, ip)
        self.graphUrl = graphUrl
