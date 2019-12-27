import re

class C():

    @staticmethod
    def solve(dic):
        soma=0 #variavel soma que é utilizada para somar a quantidade de likes

        #for que percorre o numero total de posts . i representa cada post
        for i in range(0,len(dic['posts'])):
            #seleciona o post[i] atual
            post= dic['posts'][i]
            #Expressão regular que verifica se a data do post é 02/2019
            resultmay= re.search("05/2019",post["date"])
            #Se o resultado pertence a maio de 2019
            if(resultmay!=None):
                #Expressão regular que verifica se a midia do post é instagram_cpc
                resultinsta= re.match("instagram_cpc",post["media"])
                #Expressão regular que verifica se a midia do post é google_cpc
                resultg= re.match("google_cpc",post["media"])
                #Expressão regular que verifica se a midia do post é facebook_cpc
                resultfb= re.match("facebook_cpc",post["media"])
                # Se o post esta em uma das tres midias pagas:
                if(resultinsta!=None or resultg!=None or resultfb!=None):
                    #Soma a quantidade de likes do post que passou pelas condições
                    soma+=post["likes"]                       

        #retorna a soma de likes 
        return soma




