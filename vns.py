from construtivos import *
from grasp import GRASP
from refinamento import *


def swapVNS(rota):
    i = random.randint(1, len(rota)-2) 
    j = i 
    while(j == i):
        j = random.randint(1, len(rota)-2)
    rota[i], rota[j] = rota[j], rota[i]

    return rota
    
def realocarVNS(rota):
    i = random.randint(1, len(rota)-2)
    removido = rota.pop(i)
    j = i 
    while(j == i):
        j = random.randint(1, len(rota)-2)
    rota.insert(j, removido)
    return rota

def reverterIntervaloVNS(rota):
    i = random.randint(1, len(rota)-3)
    j = random.randint(i+1, len(rota)-2)
    rota[i:j+1] = reversed(rota[i:j+1])
    return rota


def perturba(rota, k):
    if k == 1: #swap
        rota = swapVNS(rota)

    elif k == 2: #remover um e colocar entre outros
        rota = realocarVNS(rota)

    elif k == 3:
        rota = realocarVNS(rota)

    return rota

def VNS(matrizDistancias, temposInspecao):
    melhorRota, melhorCusto = guloso(matrizDistancias, temposInspecao)
    #while()
    k = 1
    while k <= 3:
        novaRota = perturba(melhorRota, k)
        novaRota, novoCusto = buscaLocal(novaRota, matrizDistancias, temposInspecao)
        if novoCusto < melhorCusto:
            melhorRota = novaRota
            melhorCusto = novoCusto
            k = 1
        else:
            k = k + 1
    return melhorRota, melhorCusto

def VNSandGRASP(matrizDistancias, temposInspecao, iMax, alpha):
    melhorRota, melhorCusto = GRASP(matrizDistancias, temposInspecao, iMax, alpha)
    k = 1
    while k <= 3:
        novaRota = perturba(melhorRota, k)
        novaRota, novoCusto = buscaLocal(novaRota, matrizDistancias, temposInspecao)
        if novoCusto < melhorCusto:
            melhorRota = novaRota
            melhorCusto = novoCusto
            k = 1
        else:
            k = k + 1
    return melhorRota, melhorCusto