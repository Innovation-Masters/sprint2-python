# Bibliotecas
import requests
from abc import ABC, abstractmethod

# Metodos
from ux.colors import *

class DockerServices(ABC):
    def __init__(self, ip: str, porta: int, serviceName: str):
        self.ip = ip
        self.porta = porta
        self.serviceName = serviceName


class ServiceBase(DockerServices):
    def __init__(self, ip: str, porta: int, serviceName: str, graphUrl=None):
        super().__init__(ip, porta, serviceName)
        self.graphUrl = graphUrl

    def checkStatus(self) -> str:
        """
        Esse metodo é utilizado para retornar o status do serviço selecionado
        :return: str
        """
        print(f"{self.ip}:{self.porta}")
        url = f"http://{self.ip}:{self.porta}/version"

        payload = ""
        headers = {}

        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            print(greenText(f"{self.serviceName}: O componente obteve sucesso ao conectar-se!"))
        except:
            print(errorText(f"{self.serviceName}: O componente demorou a responder!"))
