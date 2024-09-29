import random
import time

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
    Sorteia um destino aleatório dentro da lista simulando um possível local de corrida 

    :return: A string contendo um destino para a viagem
    """
    return random.choice(destinos)

def solicitar_preferencias():
    """
    Solicita as preferências do usuário para hotéis e passagens.

    Pergunta ao usuário se ele prefere hotéis mais baratos ou mais luxuosos
    e se prefere passagens mais econômicas ou mais confortáveis. Com base
    nas respostas, define os preços base simulados para hotéis e passagens.

    :return: tuple: Um tupla contendo o preço base do hotel e o preço base da passagem.
                     O primeiro elemento é o preço do hotel (int) e o segundo elemento
                     é o preço da passagem (int).
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
    Inicia o simulador de viagem para a corrida de Fórmula E.

    Esta função sorteia um destino, exibe informações sobre a corrida, solicita as
    preferências do usuário para hotéis e passagens, simula o transporte e os ingressos,
    e exibe o custo total da viagem.

    :return: None
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

def encontrar_hotel(preco_base):
    """
    Solicita ao usuário o número de dias de hospedagem e calcula o custo total.

    A função pede ao usuário para informar quantos dias ele deseja se hospedar e
    calcula o custo total com base no preço base fornecido. Em caso de entrada inválida,
    a função solicitará uma nova tentativa.

    :param preco_base: O preço base da diária do hotel.
    :type preco_base: float
    :return: O custo total da hospedagem.
    :rtype: float
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
    Solicita ao usuário a escolha da classe da passagem e calcula o custo total.

    A função pede ao usuário para escolher a classe da passagem (econômica, executiva ou primeira)
    e calcula o custo total com base no preço base fornecido. Em caso de entrada inválida,
    a função solicitará uma nova tentativa.

    :param preco_base: O preço base da passagem econômica.
    :type preco_base: float
    :return: O custo total da passagem.
    :rtype: float
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
    Solicita ao usuário a escolha do meio de transporte e calcula o custo total.

    A função pede ao usuário para escolher entre três meios de transporte (carro, transporte público ou táxi)
    e solicita o número de dias de utilização. Em caso de entrada inválida, a função solicitará uma nova tentativa.

    :return: O custo total do transporte.
    :rtype: float
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
    Solicita ao usuário a escolha da categoria do ingresso e calcula o custo total.

    A função pede ao usuário para escolher entre três categorias de ingressos (pista, arquibancada ou VIP).
    Em caso de entrada inválida, a função solicitará uma nova tentativa.

    :return: O custo do ingresso.
    :rtype: float
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

def exibir_total(hotel, passagem, transporte, ingresso):
    """
    Calcula e exibe o total de gastos com a viagem.

    A função soma os custos de hotel, passagem, transporte e ingresso,
    e exibe o valor total de gastos.

    :param hotel: Custo total da hospedagem.
    :type hotel: float
    :param passagem: Custo total das passagens.
    :type passagem: float
    :param transporte: Custo total do transporte.
    :type transporte: float
    :param ingresso: Custo total dos ingressos.
    :type ingresso: float
    """
    total = hotel + passagem + transporte + ingresso
    print(f"\nTotal de gastos: R${total:.2f}")
