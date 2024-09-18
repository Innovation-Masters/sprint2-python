# Cores para UX
RED = "\033[31m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Função para imprimir texto de erro
def printErrorText(text: str) -> str:
    """
    Função para imprimir textos relaiconados a erro
    :param text: O texto que terá sua cor convertida
    :return: O texto com a cor convertida
    """
    return f"{BOLD}{RED}{text}{RESET}"

def printGreenText(text: str) -> str:
    """
    Função para imprimir textos relaiconados a destaque, exemplo: escolhas de opção ou sucesso ao conectar-se
    :param text: O texto que terá sua cor convertida
    :return: O texto com a cor convertida
    """
    return f"{BOLD}{GREEN}{text}{RESET}"
