# Classes
from services.inheritances.AgentMqtt import AgentMqtt
from services.inheritances.EclipseMQTT import EclipseMQTT
from services.inheritances.Orion import Orion
from services.inheritances.Sth import Sth

# Bibliotecas
import os
from dotenv import load_dotenv

# Inicializa o .env e define o IP da máquina virtual como a variável "IP" definida no arquivo .env
load_dotenv()
dotenv_ip : str = os.getenv("IP")


# Instancia de cada serviço
agentMqtt = AgentMqtt(dotenv_ip, 4041, "Agent MQTT")
eclipseMqtt = EclipseMQTT(dotenv_ip, 1883, "Eclipse MQTT")
orion = Orion(dotenv_ip, 1026, "Orion")
sth = Sth(dotenv_ip, 8666, "STH Comet")


def services():
    """
    Função para executar o código principal do programa
    :arg dotenv_ip: IP do servidor obtido através do arquivo .env
    :return: None
    """
    print(f"{agentMqtt.checkStatus()} {eclipseMqtt.checkStatus()} {orion.checkStatus()} {sth.checkStatus()}")
