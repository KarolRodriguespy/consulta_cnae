import requests
import json
from subprocess import Popen, PIPE
import socket

url = 'https://servicodados.ibge.gov.br/api/v2/cnae/subclasses/0500301'

hostname = 'servicodados.ibge.gov.br'

class Cnae():
    def __init__(self, cnae):
        self._cnae = cnae
        
    def requisicao(self):
        result = requests.get(f'https://servicodados.ibge.gov.br/api/v2/cnae/subclasses/{self._cnae}')
        if result.status_code == 200:
            return result.json()
        else:
            return result.status_code
    
    def result(self):
        dados = self.requisicao()
        print(dados[0]['id'], dados[0]['descricao'])
        print('A Rota até os dados foi: ')
        traceroute = Popen(['tracert', hostname], stdout=PIPE)
        while True:            
            line = traceroute.stdout.readline()
            line2 = str(line).replace('\\r','').replace('\\n','') 
            print(line2)
            if not line:
                break