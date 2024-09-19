# Cores para UX
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Função para imprimir texto de erro
def errorText(text: str) -> str:
    """
    Função para imprimir textos relaiconados a erro
    :param text: O texto que terá sua cor convertida
    :return: O texto com a cor convertida
    """
    return f"{BOLD}{RED}{text}{RESET}"

def greenText(text: str) -> str:
    """
    Função para imprimir textos relaiconados a destaque, exemplo: sucesso ao conectar-se
    :param text: O texto que terá sua cor convertida
    :return: O texto com a cor convertida
    """
    return f"{BOLD}{GREEN}{text}{RESET}"

def yellowText(text: str) -> str:
    """
    Função para imprimir textos relaiconados a destaque, exemplo: escolhas de opção
    :param text: O texto que terá sua cor convertida
    :return: O texto com a cor convertida
    """
    return f"{BOLD}{YELLOW}{text}{RESET}"
