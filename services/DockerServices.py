from abc import ABC, abstractmethod

class DockerServices(ABC):
    def __init__(self, ip: str, porta: int, serviceName: str):
        self.ip = ip
        self.porta = porta
        self.serviceName = serviceName

    def checkStatus(self) -> str:
        """
        Esse metodo é utilizado para retornar o status do serviço selecionado
        :return: str
        """
        return f"IP e porta de  do serviço {self.serviceName}: {self.ip}:{self.porta} \n"

class ServiceBase(DockerServices):
    def __init__(self, ip: str, porta: int, serviceName: str, graphUrl=None):
        super().__init__(ip, porta, serviceName)
        self.graphUrl = graphUrl
