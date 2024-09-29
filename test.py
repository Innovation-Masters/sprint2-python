import requests

def healthcheck1():
    '''
    Realiza a primeira requisição de healthcheck do protocolo MQTT
    '''
    url = "http://172.201.112.163:4041/iot/about"

    payload = ""
    headers = {}

    requests.request("GET", url, headers=headers, data=payload)


  #--------health check 2.1
def healthcheck2():
    '''
    Realiza a segunda requisição de healthcheck do protocolo MQTT
    '''
    url = "http://172.201.112.163:4041/iot/services"

    payload = ""
    headers = {
      'fiware-service': 'smart',
      'fiware-servicepath': '/'
    }

    requests.request("GET", url, headers=headers, data=payload)


def healthcheck3():
    '''
    Realiza a requisição do healthcheck do serviço STH-Comet
    '''
    url = "http://172.201.112.163:8666/version"

    payload = ""
    headers = {}

    requests.request("GET", url, headers=headers, data=payload)


def healthcheck4():
    '''
    Realiza a requisição do healthcheck do serviço Orion
    '''
    url = "http://172.201.112.163:1026/version"

    payload = ""
    headers = {}

    requests.request("GET", url, headers=headers, data=payload)


try: 
    print("Conectando-se ao servidor... (1/4)")
    healthcheck1()
except TimeoutError:
    print("O componente demorou muito para responder (1/4)")
except:
    print("Ocorreu um erro (1/4)")
else:
  print("Conexão bem sucedida (1/4)")

try: 
    print("Conectando-se ao servidor... (2/4)")
    healthcheck2()
except TimeoutError:
    print("O componente demorou muito para responder (2/4)")
except:
    print("Ocorreu um erro (2/4)")
else:
  print("Conexão bem sucedida (2/4)")

try: 
    print("Conectando-se ao servidor... (3/4)")
    healthcheck3()
except TimeoutError:
    print("O componente demorou muito para responder (3/4)")
except:
    print("Ocorreu um erro (3/4)")
else:
  print("Conexão bem sucedida (3/4)")

try: 
    print("Conectando-se ao servidor... (4/4)")
    healthcheck4()
except TimeoutError:
    print("O componente demorou muito para responder (4/4)")
except:
    print("Ocorreu um erro (4/4)")
else:
  print("Conexão bem sucedida (4/4)")