from services.DockerServices import ServiceBase

from ux.colors import *

import requests
import matplotlib.pyplot as plt


class Sth(ServiceBase):
    def __init__(self, ip: str, porta: int = 8666, serviceName: str = "STH Comet"):
        super().__init__(ip, porta, serviceName)

    def obter_dados(self, atributo: str, lastN: int):
        url = f"http://{self.ip}:{self.porta}/STH/v1/contextEntities/type/Iot/id/urn:ngsi-ld:Iot:003/attributes/{atributo}?lastN={lastN}"
        headers = {
            'fiware-service': 'smart',
            'fiware-servicepath': '/'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['contextResponses'][0]['contextElement']['attributes'][0]['values']
        else:
            print(f"Erro ao obter dados de {atributo}: {response.status_code}")
            return []

    def plotar_grafico(self, dados, atributo, title):
        if not dados:
            print(f"Nenhum dado disponível para {atributo}.")
            return

        valores = [entry['attrValue'] for entry in dados]
        tempos = [entry['recvTime'] for entry in dados]

        plt.figure(figsize=(12, 6))
        plt.plot(tempos, valores, marker='o', linestyle='-', color='r')
        plt.title(f'Gráfico de {title.capitalize()} em Função do Tempo')
        plt.xlabel('Tempo')
        plt.ylabel(atributo.capitalize())
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def obter_e_plotar_dados(self):
        try:
            lastN = int(input("Escolha um valor de coletas de 1 - 100: "))
            if lastN < 1 or lastN > 100:
                return
        except ValueError:
            print(errorText("Erro: O valor informado deve ser um número inteiro"))
            return

        # Obter dados de umidade e temperatura
        dados_humidity = self.obter_dados("humidity", lastN)
        dados_temperature = self.obter_dados("temperature", lastN)

        # Plotar gráficos
        self.plotar_grafico(dados_humidity, "humidity", "Umidade")
        self.plotar_grafico(dados_temperature, "temperature", "Temperatura")

        # Obter e plotar dados de velocidade
        dados_speed = self.obter_dados("speed", lastN)
        self.plotar_grafico(dados_speed, "speed", "Velocidade")
