import requests
import json
import random
import time

# Funções para requisitar dados da API de velocidade, umidade e temperatura
def obter_dados(api_url, atributo):
    """
    Faz uma requisição GET para obter dados de um atributo (velocidade, umidade ou temperatura)
    a partir da URL fornecida da API. Retorna o valor do atributo ou None em caso de erro.

    Parâmetros:
    api_url (str): A URL da API para requisitar os dados.
    atributo (str): O nome do atributo sendo requisitado (velocidade, umidade, temperatura).

    Retorno:
    valor (int/float): O valor do atributo retornado pela API ou None em caso de erro.
    """
    try:
        headers = {
            'fiware-service': 'smart',
            'fiware-servicepath': '/',
            'accept': 'application/json'
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        dados = response.json()
        valor = dados['value']
        print(f"\n{atributo.capitalize()} atual: {valor}")
        return valor
    except requests.exceptions.RequestException as e:
        print(f"Erro ao requisitar {atributo}: {e}")
        return None

def velocidade():
    """
    Requisita e exibe a velocidade atual a partir da API.

    Retorno:
    valor (int/float): O valor da velocidade ou None em caso de erro.
    """
    return obter_dados("http://172.201.112.163:1026/v2/entities/urn:ngsi-ld:Iot:003/attrs/speed", "velocidade")

def umidade():
    """
    Requisita e exibe a umidade atual a partir da API.

    Retorno:
    valor (int/float): O valor da umidade ou None em caso de erro.
    """
    return obter_dados("http://172.201.112.163:1026/v2/entities/urn:ngsi-ld:Iot:003/attrs/humidity", "umidade")

def temperatura():
    """
    Requisita e exibe a temperatura atual a partir da API.

    Retorno:
    valor (int/float): O valor da temperatura ou None em caso de erro.
    """
    return obter_dados("http://172.201.112.163:1026/v2/entities/urn:ngsi-ld:Iot:003/attrs/temperature", "temperatura")


# Função para o simulador de viagens da Fórmula E
destinos = [
    "Nova York, Estados Unidos", 
    "Berlim, Alemanha", 
    "Tóquio, Japão", 
    "Cidade do Cabo, África do Sul", 
    "São Paulo, Brasil", 
    "Paris, França", 
    "Sydney, Austrália", 
    "Hong Kong, China", 
    "Londres, Reino Unido"
]

def sortear_destino():
    """
    Sorteia e retorna um destino de corrida da Fórmula E a partir da lista de destinos.

    Retorno:
    destino (str): O destino sorteado.
    """
    return random.choice(destinos)

def solicitar_preferencias():
    """
    Solicita as preferências do usuário para hospedagem e passagem, e retorna os preços base
    dessas escolhas.

    Retorno:
    hotel_preco_base (int): O preço base do hotel com base nas preferências do usuário.
    passagem_preco_base (int): O preço base da passagem com base nas preferências do usuário.
    """
    while True:
        try:
            preferencia_hotel = input("Você prefere hotéis mais baratos ou mais luxuosos? (1-Baratos, 2-Luxuosos): ")
            if preferencia_hotel == "1":
                hotel_preco_base = 200
                break
            elif preferencia_hotel == "2":
                hotel_preco_base = 600
                break
            else:
                raise ValueError("Escolha inválida para hotel. Digite 1 ou 2.")
        except ValueError as e:
            print(e)
    
    while True:
        try:
            preferencia_passagem = input("Você prefere passagens mais econômicas ou mais confortáveis? (1-Econômica, 2-Confortável): ")
            if preferencia_passagem == "1":
                passagem_preco_base = 1500
                break
            elif preferencia_passagem == "2":
                passagem_preco_base = 5000
                break
            else:
                raise ValueError("Escolha inválida para passagem. Digite 1 ou 2.")
        except ValueError as e:
            print(e)
    
    return hotel_preco_base, passagem_preco_base

def iniciar_simulador_viagem():
    """
    Inicia o simulador de viagem, solicita as preferências do usuário, e calcula os custos
    de hotel, passagem, transporte e ingresso. Exibe o total de gastos ao final.
    """
    destino = sortear_destino()
    print("="*50)
    print("Simulador de Viagem - Fórmula E")
    print("="*50)
    time.sleep(2)
    print(f"A próxima corrida será em {destino}")
    print("="*50)
    
    hotel_preco_base, passagem_preco_base = solicitar_preferencias()
    
    hotel = encontrar_hotel(hotel_preco_base)
    passagem = encontrar_passagem(passagem_preco_base)
    transporte = simular_transporte()
    ingresso = simular_ingressos()
    exibir_total(hotel, passagem, transporte, ingresso)


# Funções para encontrar hotel, passagem, transporte e ingressos
def encontrar_hotel(preco_base):
    """
    Calcula o custo total da hospedagem com base no número de dias fornecido pelo usuário.

    Parâmetros:
    preco_base (int): O preço base do hotel.

    Retorno:
    total (float): O custo total da hospedagem.
    """
    while True:
        try:
            dias = int(input("Quantos dias de hospedagem?: "))
            if dias <= 0:
                raise ValueError("O número de dias deve ser maior que zero.")
            total = preco_base * dias
            print(f"\nCusto total com hospedagem: R${total:.2f}")
            return total
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def encontrar_passagem(preco_base):
    """
    Calcula o custo total da passagem com base na classe escolhida pelo usuário.

    Parâmetros:
    preco_base (int): O preço base da passagem.

    Retorno:
    preco (float): O custo total da passagem (ida e volta).
    """
    while True:
        try:
            classe = int(input("Escolha a classe da passagem (1-Econômica, 2-Executiva, 3-Primeira): "))
            if classe == 1:
                preco = preco_base
            elif classe == 2:
                preco = preco_base * 2
            elif classe == 3:
                preco = preco_base * 3
            else:
                raise ValueError("Classe inválida. Digite 1, 2 ou 3.")
            print(f"Custo total com passagem: R${preco * 2:.2f}")
            return preco * 2
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def simular_transporte():
    """
    Calcula o custo total do transporte com base no tipo de transporte e número de dias
    fornecido pelo usuário.

    Retorno:
    total (float): O custo total do transporte.
    """
    while True:
        try:
            transporte = int(input("Escolha o meio de transporte (1-Carro, 2-Público, 3-Táxi): "))
            if transporte not in [1, 2, 3]:
                raise ValueError("Opção inválida. Digite 1, 2 ou 3.")
            
            dias = int(input("Por quantos dias?: "))
            if dias <= 0:
                raise ValueError("O número de dias deve ser maior que zero.")
            
            if transporte == 1:
                custo_dia = 150
            elif transporte == 2:
                custo_dia = 20
            elif transporte == 3:
                custo_dia = 100

            total = custo_dia * dias
            print(f"Custo total com transporte: R${total:.2f}")
            return total
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def simular_ingressos():
    """
    Calcula o custo total dos ingressos com base na categoria escolhida pelo usuário.

    Retorno:
    preco (float): O custo total dos ingressos.
    """
    while True:
        try:
            categoria = int(input("Escolha a categoria do ingresso (1-Pista, 2-Arquibancada, 3-VIP): "))
            if categoria == 1:
                preco = 200
            elif categoria == 2:
                preco = 400
            elif categoria == 3:
                preco = 1000
            else:
                raise ValueError("Categoria inválida. Digite 1, 2 ou 3.")
            print(f"Custo com ingresso: R${preco:.2f}")
            return preco
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")


# Função para calcular e exibir o total de gastos
def exibir_total(hotel, passagem, transporte, ingresso):
    """
    Calcula e exibe o total dos gastos com hospedagem, passagem, transporte e ingresso.

    Parâmetros:
    hotel (float): O custo total da hospedagem.
    passagem (float): O custo total da passagem.
    transporte (float): O custo total do transporte.
    ingresso (float): O custo total do ingresso.
    """
    total = hotel + passagem + transporte + ingresso
    print("="*50)
    print(f"Total estimado da viagem: R${total:.2f}")
    print("="*50)
