from services.DockerServices import ServiceBase

class Sth(ServiceBase):
    def __init__(self, ip: str, porta: int, serviceName: str):
        super().__init__(ip, porta, serviceName)

    def createGraph(self) -> str:
        """
        Com esse metodo o usuário pode gerar um gráfico com a quantidade de informações de coletas que desejar
        :return: str
        """
        return f"Gráfico gerado e adicionado ao diretorio {self.graphDir}"
