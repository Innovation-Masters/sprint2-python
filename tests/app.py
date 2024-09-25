import random
import time

possiveis_locais = [
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

def sortear_local():
    return random.choice(possiveis_locais)

local_sorteado = sortear_local()

def iniciar_programa():
    print("="*50) 
    print("Simulador de Viagem - Fórmula E")
    print("="*50)
    time.sleep(2)
    print(f"A próxima corrida será em {local_sorteado}")
    print("="*50)

def menu_inicial():
    while True:
        print("\nMENU INICIAL")
        print("1. Encontrar hotel ideal")
        print("2. Encontrar passagens de avião")
        print("3. Simular transporte no destino")
        print("4. Simular ingressos para a corrida")
        print("5. Exibir total de gastos")
        print("6. Sair")
        
        try:
            opcao = int(input("Insira uma opção: "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("Opção inválida. Escolha um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def encontrar_hotel():
    preco_base_hotel = 400
    preferencias = {
        "piscina": 40,
        "academia": 30,
        "café da manhã": 60,
        "wifi": 50,
        "transporte": 80,
        "sala de jogos": 35,
        "estacionamento": 20
    }
    
    print("\nResponda as seguintes perguntas para entendermos suas preferências.")
    time.sleep(1)
    print("Para adicionar a preferência, digite 's' (sim), caso contrário digite 'n' (não).\n")
    
    for item, valor in preferencias.items():
        while True:
            preferencia = input(f"Seu hotel ideal precisa ter {item}? (s/n): ").lower()
            if preferencia in ['s', 'n']:
                break
            else:
                print("Entrada inválida. Digite 's' para sim ou 'n' para não.") 
        
        if preferencia == "s":
            preco_base_hotel += valor
    
    while True:
        try:
            dias = int(input("Quantos dias você pretende passar na viagem?: "))
            break
        except ValueError:
            print("Insira um número válido de dias.")
    
    preco_final_hotel = preco_base_hotel * dias
    
    print(f"\nEm {dias} dias de viagem, você gastará R${preco_final_hotel:.2f} com hospedagem.")
    time.sleep(2)
    return preco_final_hotel

def encontrar_passagem():
    while True:
        print("\nEscolha a classe da sua passagem:")
        print("1. Econômica")
        print("2. Executiva")
        print("3. Primeira classe")
        
        try:
            opcao_passagem = int(input("Insira uma opção para suas passagens (1/2/3): "))
            if opcao_passagem == 1:
                preco_passagem = 3000 * 2
                break
            elif opcao_passagem == 2:
                preco_passagem = 5000 * 2
                break
            elif opcao_passagem == 3:
                preco_passagem = 7500 * 2
                break
            else:
                print("Opção inválida. Escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")
    
    print(f"Você gastará R${preco_passagem:.2f} com passagens de ida e volta.")
    time.sleep(2)
    return preco_passagem

def simular_transporte():
    print("\nEscolha o meio de transporte:")
    print("1. Alugar um carro (R$ 150 por dia)")
    print("2. Usar transporte público (R$ 20 por dia)")
    print("3. Andar de táxi ou ride-sharing (R$ 100 por dia)")
    
    while True:
        try:
            opcao_transporte = int(input("Escolha uma opção (1/2/3): "))
            if opcao_transporte == 1:
                preco_transporte = 150
                meio_transporte = "Aluguel de carro"
                break
            elif opcao_transporte == 2:
                preco_transporte = 20
                meio_transporte = "Transporte público"
                break
            elif opcao_transporte == 3:
                preco_transporte = 100
                meio_transporte = "Táxi ou ride-sharing"
                break
            else:
                print("Opção inválida. Escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")
    
    while True:
        try:
            dias_transporte = int(input("Por quantos dias você usará o transporte?: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número de dias válido.")
    
    custo_total_transporte = preco_transporte * dias_transporte
    print(f"\nVocê escolheu {meio_transporte}. O custo total será R${custo_total_transporte:.2f}.")
    time.sleep(2)
    return custo_total_transporte

def simular_ingressos():
    print("\nEscolha a categoria do ingresso para a corrida:")
    print("1. Pista (R$ 200)")
    print("2. Arquibancada (R$ 400)")
    print("3. VIP (R$ 1000)")
    
    while True:
        try:
            opcao_ingresso = int(input("Escolha uma opção (1/2/3): "))
            if opcao_ingresso == 1:
                preco_ingresso = 200
                break
            elif opcao_ingresso == 2:
                preco_ingresso = 400
                break
            elif opcao_ingresso == 3:
                preco_ingresso = 1000
                break
            else:
                print("Opção inválida. Escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")
    
    print(f"Você gastará R${preco_ingresso:.2f} pelo ingresso.")
    time.sleep(2)
    return preco_ingresso

def exibir_total(hotel=0, passagem=0, transporte=0, ingresso=0):
    total = hotel + passagem + transporte + ingresso
    print(f"\nTotal estimado de gastos: R${total:.2f}\n")
    time.sleep(2)

# Variáveis para acumular o valor total gasto em cada seção
total_hotel = 0
total_passagem = 0
total_transporte = 0
total_ingresso = 0

iniciar_programa()

while True:
    opcao = menu_inicial()

    if opcao == 1:
        total_hotel = encontrar_hotel()
    elif opcao == 2:
        total_passagem = encontrar_passagem()
    elif opcao == 3:
        total_transporte = simular_transporte()
    elif opcao == 4:
        total_ingresso = simular_ingressos()
    elif opcao == 5:
        exibir_total(total_hotel, total_passagem, total_transporte, total_ingresso)
    elif opcao == 6:
        print("Saindo do programa...")
        break
