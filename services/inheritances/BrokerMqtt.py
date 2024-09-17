from services.DockerServices import ServiceBase

class BrokerMqtt(ServiceBase):
    def __init__(self, porta, ip):
        super().__init__(porta, ip)
