from services.DockerServices import ServiceBase

class Orion(ServiceBase):
    def __init__(self, ip: str, porta: int, serviceName: str):
        super().__init__(ip, porta, serviceName)
