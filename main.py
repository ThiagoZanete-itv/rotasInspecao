from grasp import *
from vns import *
from dados import *
from geradordenos import *
from scipy.stats import wilcoxon
import matplotlib.pyplot as plt 

import time
import numpy as np

CAMINHOVNS = "C:/Users/c0771/Documents/OneDrive - ASSOCIACAO INSTITUTO TECNOLOGICO VALE - ITV/ic/VNSresults.xlsx"
CAMINHOGRASP = "C:/Users/c0771/Documents/OneDrive - ASSOCIACAO INSTITUTO TECNOLOGICO VALE - ITV/ic/GRASPresults.xlsx"
N_EXEC = 30
N_NOS = 80
ALPHA = 0.1

def main():
    #matrizExemplo = [[0,25,125,225,475,275],[25,0,125,200,450,250],[125,125,0,175,375,125],[225,200,175,0,175,225],[475,450,375,175,0,250],[275,250,125,225,250,0]]
    #temposInspecao = [0,0,0,0,0,0,0,0,0,0]
    #matrizExemplo, temposInspecao = lerDados(CAMINHOPLANILHA)
    print(f"Gerando {N_NOS} nos ...")
    matrizExemplo, temposInspecao = gerarInstancia(N_NOS)
    print("Matriz de nos gerada")
    #print(matrizExemplo, temposInspecao)

    rotaTeste, custoteste = guloso(matrizExemplo,temposInspecao)
    print("\nGuloso: ", custoteste )
    #print("\nGRASP: ", rotaTeste, custoteste )

    #executar várias vezes
    print("\nExecutando VNS ...")
    inicio = time.perf_counter()
    piorCusto = 0
    melhorCusto = float('inf')
    custosVNS = []
    resultados = []
    for i in range(N_EXEC):
        rota2, custo2 = VNS(matrizExemplo, temposInspecao)
        resultados.append({"rota: ": rota2, "custo": custo2})
        custosVNS.append(custo2)
        if custo2 > piorCusto:
            piorCusto = custo2
        elif custo2 < melhorCusto:
            melhorCusto = custo2
            rota = rota2.copy()
    fim = time.perf_counter()

    print(f"Melhor custo: {melhorCusto:.2f}")
    print(f"media: {np.mean(custosVNS):.2f}" f"    desvio: {np.std(custosVNS):.2f}" f"    mediana: {np.median(custosVNS):.2f}")
    print(f"Tempo total: {(fim - inicio):.3f}s", f"Tempo médio: {(fim - inicio)/N_EXEC:.3f}s")
    #escreverDados(CAMINHOVNS, resultados)
    #fim das execuções do VNS
   
    
    '''
    for i in range(10):
        r, t = parcGuloso(matrizExemplo, 0.4, temposInspecao)
        print("Antes BL:", t)
        r2, t2 = buscaLocal(r.copy(),matrizExemplo,temposInspecao)
        print("Depois BL:", t2)
        print()
    return 0
    '''

    #executar várias vezes
    print("\nExecutando GRASP ...")
    inicio = time.perf_counter()
    piorCusto = 0
    melhorCusto = float('inf')
    custosGRASP = []
    resultados = []
    for i in range(N_EXEC):
        rota2, custo2 = GRASP(matrizExemplo, temposInspecao, 15, ALPHA)
        resultados.append({"rota: ": rota2, "custo": custo2})
        custosGRASP.append(custo2)
        if custo2 > piorCusto:
            piorCusto = custo2
        elif custo2 < melhorCusto:
            melhorCusto = custo2
            rota = rota2.copy()
        #print(rota2, custo2)
    fim = time.perf_counter()

    print(f"Melhor custo: {melhorCusto:.2f}")
    print(f"media: {np.mean(custosGRASP):.2f}" f"    desvio: {np.std(custosGRASP):.2f}" f"    mediana: {np.median(custosGRASP):.2f}")
    print(f"Tempo total: {(fim - inicio):.3f}s", f"Tempo médio: {(fim - inicio)/N_EXEC:.3f}s")
    #escreverDados(CAMINHOGRASP, resultados)   
    
#executar várias vezes
    print("\nExecutando VNSandGRASP ...")
    inicio = time.perf_counter()
    piorCusto = 0
    melhorCusto = float('inf')
    custosVNSandGRASP = []
    resultados = []
    for i in range(N_EXEC):
        rota2, custo2 = VNSandGRASP(matrizExemplo, temposInspecao, 15, ALPHA)
        resultados.append({"rota: ": rota2, "custo": custo2})
        custosVNSandGRASP.append(custo2)
        if custo2 > piorCusto:
            piorCusto = custo2
        elif custo2 < melhorCusto:
            melhorCusto = custo2
            rota = rota2.copy()
        #print(rota2, custo2)
    fim = time.perf_counter()

    print(f"Melhor custo: {melhorCusto:.2f}")
    print(f"media: {np.mean(custosVNSandGRASP):.2f}" f"    desvio: {np.std(custosVNSandGRASP):.2f}" f"    mediana: {np.median(custosVNSandGRASP):.2f}")
    print(f"Tempo total: {(fim - inicio):.3f}s", f"Tempo médio: {(fim - inicio)/N_EXEC:.3f}s")
    #escreverDados(CAMINHOGRASP, resultados)   



    #resultadso estastistiscos
    stats, p = wilcoxon(custosVNS, custosGRASP)
    print("\n", p, "\n")
    '''
    #boxplot
    plt.figure(figsize=(8,5))
    plt.boxplot([custosVNS, custosGRASP], tick_labels=["VNS", "GRASP"])
    plt.ylabel("Custo")
    plt.title("Comparação dos custos obtidos pelos algoritmos")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.show()
    '''
    
    instancias = range(1, len(custosVNS)+1)
    plt.figure(figsize=(10,5))
    plt.plot(instancias, custosVNS, marker='+', label='VNS')
    plt.plot(instancias, custosGRASP, marker='*', label='GRASP')
    plt.plot(instancias, custosVNSandGRASP, marker='.', label='VNSandGRASP')
    plt.xlabel("Execução")
    plt.ylabel("Custo")
    plt.title("Desempenho por execução")
    plt.legend()
    plt.grid(True)
    plt.show()


    return 0
    
    #print("Vetor de Tempos: ", tempos)  
    #print("VNS: ", rota, "piorCusto: ", piorCusto, "melhorCusto: ", melhorCusto, "custoMedio: ", sum(tempos)/len(tempos))
    #rota, tempo = GRASP(matrizExemplo,temposInspecao,10,0)
    #print("GRASP: ", rota, tempo)
    inicio = time.perf_counter()
    rota, tempo = guloso(matrizExemplo,temposInspecao)
    fim = time.perf_counter()
    print("Tempo e execução guloso: ", (fim-inicio), "s")
    print("Guloso: ", rota, tempo)

    inicio = time.perf_counter()
    rota, tempo = parcGuloso(matrizExemplo, 0.3, temposInspecao)
    fim = time.perf_counter()
    print("Tempo de execução Parc Guloso: ", (fim-inicio), "s")
    print("Parc Guloso: ", rota, tempo)

main()