# Bibliotecas
import os

# Import das funções para serem executadas no programa principal
from functions.services import services
from ux.colors import errorText
from ux.colors import greenText
from ux.colors import yellowText

# Divisor para o painel
divider = "=-" * 22

def main():
    """
    Função que executa o painel principal do programa
    :return:
    """
    print(divider)
    print("1 - Verificar status dos serviços")
    print("2 - Opção dois")
    print("3 - Opção três")
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
            services()
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
