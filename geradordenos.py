import random 
#import pandas as pd

def gerarInstancia(n):
    matriz = [[0]*n for _ in range(n)]
    for i in range (n):
        for j in range(i+1, n):
            d = round(random.uniform(10, 500),3)
            matriz[i][j] = d
            matriz[j][i] = d 
    tempos = [0.0]
    for _ in range(n-1):
        tempos.append(round(random.uniform(1, 120),3))

    return matriz, tempos