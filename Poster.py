import json
import requests 
import os

class Poster():

    #Cria o arquivo resposta.json com o dicionario de respostas
    #Efetua requisição post para a API RaccoonPoster
    #Recebe a resposta da requisição post
    @staticmethod
    def post(resposta):
        #Escreve a resposta dos exercícios no arquivo resposta.json em json
        with open('resposta.json','w') as f:
            json.dump(resposta,f,indent=4)
            
        os.system("curl -H \"Content-Type: application/json\"--data @resposta.json https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_post")
        
        return 
