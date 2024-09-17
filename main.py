# Bibliotecas
import os
from dotenv import load_dotenv

from app import main # Metodo principal do programa

load_dotenv() # Inicializa o .env
dotenv_ip = os.getenv("IP") # Define o IP da máquina virtual como a variável "IP" definida no arquivo .env
os.system("cls") # Limpa o prompt de comando para uma melhor visualização dos dados

# Executa o código principal do programa
if __name__ == '__main__':
    main(dotenv_ip)
