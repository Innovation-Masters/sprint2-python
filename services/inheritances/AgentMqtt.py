from services.DockerServices import ServiceBase

class AgentMqtt(ServiceBase):
    def __init__(self, porta: str, ip: int):
        super().__init__(porta, ip)
