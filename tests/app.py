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
        print("3. Outra opção")
        print("4. Outra opção")
        print("5. Sair")
        
        try:
            opcao = int(input("Insira uma opção: "))
            if 1 <= opcao <= 5:
                return opcao
            else:
                print("Opção inválida. Escolha um número entre 1 e 5.")
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

iniciar_programa()

while True:
    opcao = menu_inicial()

    if opcao == 1:
        encontrar_hotel() 
    elif opcao == 2:
        encontrar_passagem() 
    elif opcao == 3:
        print("Em breve!")
    elif opcao == 4:
        print("Em breve!")
    elif opcao == 5:
        print("Saindo do programa...")
        break
