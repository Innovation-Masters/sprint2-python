from services.DockerServices import ServiceBase

class Sth(ServiceBase):
    def __init__(self, porta, graphDir, ip):
        super().__init__(porta, ip, graphDir)

    def createGraph(self) -> str:
        return f"Gráfico gerado e adicionado ao diretorio {self.graphDir}"
