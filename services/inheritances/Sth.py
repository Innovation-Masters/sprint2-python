from services.DockerServices import ServiceBase

class Sth(ServiceBase):
    def __init__(self, porta: int, graphDir: str, ip: str):
        super().__init__(porta, ip, graphDir)

    def createGraph(self) -> str:
        """
        Com esse metodo o usuário pode gerar um gráfico com a quantidade de informações de coletas que desejar
        :return: str
        """
        return f"Gráfico gerado e adicionado ao diretorio {self.graphDir}"
