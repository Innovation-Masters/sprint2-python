# from functions.panel import main
from services.DockerServices import ServiceBase

class Orion(ServiceBase):
    def __init__(self, ip: str, porta: int = 1026, serviceName: str = "Orion Context Broker"):
        super().__init__(ip, porta, serviceName)
