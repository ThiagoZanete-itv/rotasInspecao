
from construtivos import *
from refinamento import *


def GRASP(matrizDistancias, temposInspecao, iMax, alpha):
    #rotaAtual = []
    #tempoAtual = float('inf')
    rotaAtual, tempoAtual = guloso(matrizDistancias, temposInspecao)
    #colocar guloso aqui, trocar perturbações no vns
   
    i = 0
    while(i < iMax):
        r2, t2 = parcGuloso(matrizDistancias, alpha, temposInspecao)
        #print("\n\n", t2, '\n\n')
        r2, t2 = buscaLocal(r2, matrizDistancias, temposInspecao)
        #print("\n\n", t2, '\n\n')
        if(t2 < tempoAtual):
            rotaAtual = r2
            tempoAtual = t2
            i = 0
        #print(i)
        i = i + 1
    return rotaAtual, tempoAtual