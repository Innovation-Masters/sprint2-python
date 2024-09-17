from services.DockerServices import ServiceBase

class BrokerMqtt(ServiceBase):
    def __init__(self, porta: int, ip: str):
        super().__init__(porta, ip)
