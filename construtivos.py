import random

def guloso(matrizDistancias, temposInspecao):
    n = len(matrizDistancias)
    candidatos = set(range(1, n))
    pAtual = 0
    rota = [0]
    tempo = 0
    while(candidatos):
        proxPonto = min(candidatos, key=lambda i: matrizDistancias[pAtual][i] + temposInspecao[i])
        tempo += matrizDistancias[pAtual][proxPonto] + temposInspecao[proxPonto]
        rota.append(proxPonto)
        candidatos.remove(proxPonto)
        pAtual = proxPonto
    rota.append(0)
    tempo += matrizDistancias[pAtual][0]
    return rota, tempo


def parcGuloso(matrizDistancias, alpha, temposInspecao):
    n = len(matrizDistancias)
    candidatos = set(range(1, n))
    pAtual = 0
    tempo = 0
    rota = [0]

    while(candidatos):
        gmin = min(matrizDistancias[pAtual][i] + temposInspecao[i] for i in candidatos)
        gmax = max(matrizDistancias[pAtual][i] + temposInspecao[i] for i in candidatos)
        lcr = []
        for i in candidatos:
            if matrizDistancias[pAtual][i] + temposInspecao[i] <= gmin + alpha * (gmax - gmin):
                lcr.append(i)
        #print(len(lcr))
        proxPonto = random.choice(lcr)
        tempo += matrizDistancias[pAtual][proxPonto] + temposInspecao[proxPonto]
        rota.append(proxPonto)
        candidatos.remove(proxPonto)
        pAtual = proxPonto

    rota.append(0)
    tempo += matrizDistancias[pAtual][0]
        
    return rota, tempo

