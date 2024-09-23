import random
import time

possiveis_locais = ["Nova York, Estados Unidos", "Berlim, Alemanha", "Tóquio, Japão", "Cidade do Cabo, África do Sul", "São Paulo, Brasil", "Paris, França", "Sydney, Austrália", "Hong Kong, China", "Londres, Reino Unido",]

def sortear_local():
    local = possiveis_locais[random.randint(0,8)]
    return local

local_sorteado = sortear_local()

def iniciar_programa():
    print("="*50) 
    print("Simulador de Viagem - Fórmula E")
    print("="*50)
    time.sleep(2)
    print(f"A próxima corrida será em {local_sorteado}")
    print("="*50)


def menu_inicial():
    print("1. Encontrar hotel ideal")
    print("2.")
    print("3.")
    print("4.")
    print("5.")


def encontrar_hotel():
    preco_base_hotel = 400
    preferencias = {
        "piscina": 40,
        "academia": 30,
        "café da manha": 60,
        "wifi": 50,
        "transporte": 80,
        "sala de jogos": 35,
        "estacionamento": 20
    }
    print("Responda as seguintes perguntas para entendermos suas preferências")
    time.sleep(1)
    print("Para adicionar a preferência digite 's', caso contrário digite qualquer tecla \n")
    for item in preferencias:
        preferencia = input(f"Seu hotel ideal precisa ter {item}?: ").lower()
        
        if preferencia == "s":
            valor = preferencias[item]
            preco_base_hotel += valor


iniciar_programa()
