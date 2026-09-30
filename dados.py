from sqlite3 import DatabaseError

import pandas as pd
import openpyxl

def lerDados(caminhoPlanilha):
    distancias = pd.read_excel(caminhoPlanilha,sheet_name= "locais", header = None)
    tempos = pd.read_excel(caminhoPlanilha, sheet_name= "tempos")

    distancias2 = distancias.values.tolist()
    tempos2 = tempos.values.tolist()

    return distancias2, tempos2

def escreverDados(caminhoPlanilha, dados):
    df = pd.DataFrame(dados)
    df.to_excel(caminhoPlanilha,sheet_name= "vns")