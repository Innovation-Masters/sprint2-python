# Bibliotecas
import os

# Import das funções para serem executadas no programa principal
from functions.services import services
from ux.colors import printErrorText
from ux.colors import printGreenText

# Divisor para o painel
divider = "=-=" * 14

def main():
    """
    Função que executa o painel principal do programa
    :return:
    """
    print(divider)
    print("1 - Verificar status dos serviços")
    print("2 - Jogo da velha falsificado")
    print("3 - Me da um real ae")
    print("4 - Encerrar Programa")
    print(divider)
    try:
        option = int(input(printGreenText("Selecione uma opção: ")))
    except ValueError as error:
        print(printErrorText(f"ERRO {error}"))

    match option:
        case 1:
            os.system("cls")
            services()
        case __:
            print(printErrorText("Opção inválida! Programa encerrado"))
            exit()
