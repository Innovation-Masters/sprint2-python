# Classes
# from services.inheritances.AgentMqtt import AgentMqtt
from services.inheritances.BrokerMqtt import BrokerMqtt
# from services.inheritances.Orion import Orion
# from services.inheritances.Sth import Sth


def main(dotenv_ip: str):
    """
    Função para executar o código principal do programa
    :arg dotenv_ip: IP do servidor obtido através do arquivo .env
    :return: None
    """
    service = BrokerMqtt(123, dotenv_ip) # Instancia do objeto (BrokerMQTT)
    check_status = service.checkStatus() # Checa o status do serviço (BrokerMQTT)
    print(check_status) # Printa o valor do serviço (BrokerMQTT)
