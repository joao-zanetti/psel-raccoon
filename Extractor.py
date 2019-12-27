import json
import requests 

class Extractor():
    
    #Retorna dicionario com as resposta da requicisao get
    @staticmethod
    def get(URL):
        # api-endpoint 
        # sending get request and saving the response as response object 
        r = requests.get(URL) 
        # extracting data in json format 
        d = r.json()
        return d

    