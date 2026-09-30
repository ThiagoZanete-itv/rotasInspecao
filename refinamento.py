def calCusto(rota, matrizDistancias, temposInspecao):
    custo = 0
    for i in range(len(rota)-1):
        origem = rota[i]
        destino = rota[i+1]
        custo += matrizDistancias[origem][destino]

        if destino != 0:
            custo += temposInspecao[destino]
    return custo



def buscaLocal(rota, matrizDistancias, temposInspecao):
    melhorou = True
    rota2 = rota.copy()
    while melhorou:
        melhorou = False
        custoAtual = calCusto(rota2, matrizDistancias, temposInspecao)
        for i in range(1, len(rota2)-2):
            for j in range(i+1, len(rota2)-1):
                   novaRota = rota2.copy()
                   novaRota[i], novaRota[j] = novaRota[j], novaRota[i]
                   novoCusto = calCusto(novaRota, matrizDistancias, temposInspecao)
                   if novoCusto < custoAtual:
                       rota2 = novaRota
                       custoAtual = novoCusto
                       melhorou = True
                       break
                   
            if melhorou:
                break
    return rota2, custoAtual   