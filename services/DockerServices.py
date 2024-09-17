from abc import ABC, abstractmethod

class DockerServices(ABC):
    def __init__(self, porta: int, ip: str):
        self.porta = porta
        self.ip = ip

    def checkStatus(self) -> str:
        """
        Esse metodo é utilizado para retornar o status do serviço selecionado
        :return: str
        """
        return f"IP e porta de conexão: {self.ip}:{self.porta}"

class ServiceBase(DockerServices):
    def __init__(self, porta: int, ip: str, graphUrl=None) -> None:
        super().__init__(porta, ip)
        self.graphUrl = graphUrl
