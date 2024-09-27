# from functions.panel import main
from services.DockerServices import ServiceBase

class AgentMqtt(ServiceBase):
    def __init__(self, ip: str, porta: int = 4041, serviceName: str = "AgentMQTT"):
        super().__init__(ip, porta, serviceName)
