import re

class A():

    @staticmethod
    def solve(dic):
        response_avec=[] #vetor da resposta a
        response_aux={} #dicionario auxiliar que é utilizado para preencher cada produto que passa as condições
        repetition={} #dicionario que verifica a repeticao de product_ids

        #for que percorre todos os posts
        #i representa cada post 
        for i in range(0,len(dic['posts'])):

            #seleciona o post[i] atual
            post= dic['posts'][i]
            #expressão regular que busca a palavra promocao no titulo do respectivo post[i]
            result= re.search("promocao",post["title"])

            # Se o produto esta em promocao:
            if(result!=None):
                #Se o product_id ja esta no dicionario de repeticoes:
                if post["product_id"] in repetition:
                    repetition[post["product_id"]]=repetition[post["product_id"]]+1
                #Se o product_id nao esta no dicionario de repeticoes
                else:  
                    #Adiciona o product_id no vetor de repeticoes
                    repetition[post["product_id"]]=1
                    #Preenche o dicionario auxiliar com product_id e preço do respectivo produto
                    response_aux["product_id"]=post["product_id"]
                    response_aux["price_field"]=post["price"]
                    #Adiciona o dicionario preenchido com o post atual no vetor resultado
                    response_avec.append(response_aux)
                    response_aux={}

        #ordenando o vetor de dicionários, resposta, primeiro pelo preço, e em caso de empate, pelo post id
        response_a= sorted(response_avec,key=lambda k: (k["price_field"],k["product_id"]))
        #retorna vetor de resposta ordenado 
        return response_a
