class D():

    @staticmethod
    def solve(dice):
        repetition={} #dicionario que verifica repeticao de product_ids e seu primeiro preco lido
        response_error=[] #vetor no qual cada elemento inserido, é um product id com erro 

        #for que percorre todos os posts
        #i representa cada post 
        for i in range(0,len(dice['posts'])):
            post= dice['posts'][i]
            #Se o product_id ja esta no dicionario de repeticoes:
            #ou seja, se product_id ja foi lido
            if post["product_id"] in repetition:
                #Se o preço do product_id atual é diferente do preço já lido deste produto
                if(repetition[post["product_id"]]!=post["price"]):
                    #Se o product_id não esta na lista de erro
                    if(post["product_id"] not in response_error):
                        response_error.append(post["product_id"])
            #Se o preço do respectivo product_id ainda não foi lido
            else:  
                #Insere o product_id com seu respectivo preço no dicionario de repeticoes
                repetition[post["product_id"]]=post["price"]

        #ordenando o vetor resposta pelo product_id
        response_d= sorted(response_error)
        #retorna vetor de resposta ordenado 
        return response_d