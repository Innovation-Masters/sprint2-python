# Bibliotecas
import os
from dotenv import load_dotenv

# Classes
from services.inheritances.AgentMqtt import AgentMqtt
from services.inheritances.Orion import Orion
from services.inheritances.Sth import Sth

# Import das funções para serem executadas no programa principal
from ux.colors import errorText
from ux.colors import greenText
from ux.colors import yellowText

# Import da função do painel de simulação de viagens
from functions.travelSimulator import iniciar_simulador_viagem

# Inicializa o .env e define o IP da máquina virtual como a variável "IP" definida no arquivo .env
load_dotenv()
dotenv_ip = os.getenv("IP")

# Instancia de cada serviço
agentMqtt = AgentMqtt(dotenv_ip)
orion = Orion(dotenv_ip)
sth = Sth(dotenv_ip)

# Divisor para o painel
divider = "=-" * 22

def main():
    """
    Função que executa o painel principal do programa
    :return:
    """
    print(divider)
    print("1 - Verificar status dos serviços")
    print("2 - Simulador de viagens")
    print("3 - Acessar Dados em um gráfico plotado")
    print("4 - Encerrar Programa")
    print(divider)

    # Verifica se o número fornecido pelo usuário é um inteiro, caso contrário, imprime uma mensagem de erro e retorna a execução do programa
    try:
        option = int(input(yellowText("-> Selecione uma opção: ")))
    except:
        print(errorText(divider))
        print(errorText(f"O programa aceita somente números inteiros!"))
        print(errorText(divider))
        main()

    # Trata a opção que o usuário escolher e inicia a função adequada no "./functions"
    match option:
        case 1:
            os.system("cls")
            sth.checkStatus()
            orion.checkStatus()
            agentMqtt.checkStatus()
            main()
        case 2:
            os.system("cls")
            iniciar_simulador_viagem()
            main()
        case 3:
            sth.obter_e_plotar_dados()
            os.system("cls")
            main()
        case 4:
            print(greenText(divider))
            print(greenText("Programa encerrado com sucesso!"))
            print(greenText(divider))
            exit()
        # Caso o usuário digite uma opção inexistente, o programa é reiniciado
        case __:
            print(errorText(divider))
            print(errorText("Opção inexistente!"))
            print(errorText(divider))
            main()
