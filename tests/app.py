import requests
import json
import random
import time

# Funções para requisitar dados da API de velocidade, umidade e temperatura
def obter_dados(api_url, atributo):
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
    return obter_dados("http://{ip}/v2/entities/urn:ngsi-ld:Iot:003/attrs/speed", "velocidade")

def umidade():
    return obter_dados("http://{ip}/v2/entities/urn:ngsi-ld:Iot:003/attrs/humidity", "umidade")

def temperatura():
    return obter_dados("http://{ip}/v2/entities/urn:ngsi-ld:Iot:003/attrs/temperature", "temperatura")


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
    return random.choice(destinos)

def solicitar_preferencias():
    while True:
        try:
            preferencia_hotel = input("Você busca hotéis mais baratos ou mais luxuosos? (1-Baratos, 2-Luxuosos): ")
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
    while True:
        try:
            dias = int(input("Quantos dias de hospedagem?: "))
            if dias <= 0:
                raise ValueError("O número de dias deve ser maior que zero.")
            total = preco_base * dias
            print(f"\nCusto da hospedagem: R${total:.2f}")
            return total
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def encontrar_passagem(preco_base):
    while True:
        try:
            classe = int(input("Escolha a classe da passagem (1-Econômica, 2-Executiva, 3-Primeira classe): "))
            if classe == 1:
                preco = preco_base
            elif classe == 2:
                preco = preco_base * 2
            elif classe == 3:
                preco = preco_base * 3
            else:
                raise ValueError("Classe inválida. Digite 1, 2 ou 3.")
            print(f"Custo das passagens (ida e volta): R${preco * 2:.2f}")
            return preco * 2
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def simular_transporte():
    while True:
        try:
            transporte = int(input("Escolha o meio de transporte durante a viagem (1-Carro alugado, 2-Transporte público, 3-Táxi): "))
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
            print(f"Custo dos transporte: R${total:.2f}")
            return total
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def simular_ingressos():
    while True:
        try:
            categoria = int(input("Escolha a categoria do ingresso (1-Meia, 2-Inteira, 3-VIP): "))
            if categoria == 1:
                preco = 200
            elif categoria == 2:
                preco = 400
            elif categoria == 3:
                preco = 1000
            else:
                raise ValueError("Categoria inválida. Digite 1, 2 ou 3.")
            print(f"Custo dos ingressos: R${preco:.2f}")
            return preco
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")


# Função para calcular e exibir total de gastos
def exibir_total(hotel, passagem, transporte, ingresso):
    total = hotel + passagem + transporte + ingresso
    print(f"\nTotal de gastos: R${total:.2f}")


# Menu principal
def menu_principal():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Visualizar Velocidade")
        print("2. Visualizar Umidade")
        print("3. Visualizar Temperatura")
        print("4. Simulador de Viagem")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            velocidade()
        elif opcao == "2":
            umidade()
        elif opcao == "3":
            temperatura()
        elif opcao == "4":
            iniciar_simulador_viagem()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa
menu_principal()
