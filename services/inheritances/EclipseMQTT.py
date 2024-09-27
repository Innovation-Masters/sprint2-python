# from functions.panel import main
from services.DockerServices import ServiceBase

class EclipseMQTT(ServiceBase):
    def __init__(self, ip: str, porta: int = 1883, serviceName: str = "EclipseMQTT"):
        super().__init__(ip, porta, serviceName)
