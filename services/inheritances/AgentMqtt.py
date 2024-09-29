# from functions.panel import main
from services.DockerServices import ServiceBase

# Metodos
from ux.colors import *

class AgentMqtt(ServiceBase):
    def __init__(self, ip: str, porta: int = 4041, serviceName: str = "AgentMQTT"):
        super().__init__(ip, porta, serviceName)


    def checkStatus(self) -> str:
        """
        Esse metodo é utilizado para retornar o status do serviço selecionado
        :return: str
        """
        print(f"{self.ip}:{self.porta}")
        url = f"http://{self.ip}:{self.porta}/iot/about"

        payload = ""
        headers = {}

        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            print(greenText(f"{self.serviceName}: O componente obteve sucesso ao conectar-se!"))
        except:
            print(errorText(f"{self.serviceName}: O componente demorou a responder!"))
