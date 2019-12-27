from Extractor import * #Classe que efetua requisições get para API RaccoonExtractor
from A import * #Classe que resolve ex a)
from B import * #Classe que resolver ex b)
from C import * #Classe que resolver ex c)
from D import * #Classe que resolver ex d)
from Poster import * #Classe que efetua requisição post para API para API RaccoonPoster

#Dicionário que armazena as respostas de todos exercícios (a,b,c,d)
#Será escrito no arquivo resposta.json
resposta = {}

#Metodo get() da Classe Extactor, retorna dicionario com as resposta da requisiçao get
#parametro da funcao: url da API que recebe o get
get=Extractor.get("https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get") 
get_error=Extractor.get("https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get_error") 

#Metodo solve() da Classe A, retorna uma lista de dicionarios
#Com os IDs dos produtos que contém "promoção" no título e seus respectivos preços para todas as mídias. 
#O resultado é ordenado por preço e depois ID, de forma CRESCENTE. Sem IDs de produtos repetidos
response_a =A.solve(get)

#Metodo solve() da Classe B, retorna uma lista de dicionarios   
#Com os IDs dos posts que contém mais de 700 likes na mídia instagram_cpc. 
#O resultado é ordenado por preço e depois ID, de forma CRESCENTE.
response_b= B.solve(get)

#Metodo solve() da Classe C, retorna um int:
#Somatório de likes no mês de maio de 2019 para todas as mídias pagas (google_cpc, facebook_cpc,instagram_cpc).
response_c= C.solve(get)

#Metodo solve() da Classe D, retorna uma lista:
#Caso seja encontrado algum erro, retorna lista com todos os IDs de produtos com erro de forma ordenada
response_d= D.solve(get_error)

#Campos inseridos na resposta
resposta["full_name"]="Joao Renato Zanetti de Lima"
resposta["email"]="j.zanettilima@gmail.com"
resposta["code_link"]="www.github.com/joao-zanetti/psel-raccoon"
resposta["response_a"]=response_a 
resposta["response_b"]=response_b
resposta["response_c"]=response_c
resposta["response_d"]=response_d

#print(resposta)

#Metodo post() da Classe Poster, cria o arquivo resposta.json com o dicionario de respostas,
#faz requisição post para API RaccoonPoster
Poster.post(resposta)




