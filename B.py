import re

class B():

    @staticmethod
    def solve(dic):
        response_bvec=[] #vetor da resposta b
        response_aux={} #dicionario auxiliar que é utilizado para preencher cada post que passa as condições

        #for que percorre o numero total de posts
        #i representa cada post
        for i in range(0,len(dic['posts'])):

            #seleciona o post[i] atual
            post= dic['posts'][i]
            #expressão regular que verifica se o post atual pertence a midia instagram_cpc
            result= re.match("instagram_cpc",post["media"])

            # Se o post esta na midia instagram_cpc:
            if(result!=None):
                #Se o post tem mais de 700 likes
                if(post["likes"]>700):
                    #preenche post_id e price_field do dicionario b
                    response_aux["post_id"]=post["post_id"] 
                    response_aux['price_field']=post["price"]
                    #insere o dicionario b no vector 
                    response_bvec.append(response_aux)
                    response_aux={}

        #ordenando o vetor de dicionários, resposta, primeiro pelo preço, e em caso de empate, pelo post id
        response_b= sorted(response_bvec,key=lambda k: (k['price_field'],k["post_id"]))
        #retorna vetor de resposta ordenado 
        return response_b