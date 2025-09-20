# Funções ----------------------------------------------------------------------
import pandas as pd
df = pd.read_csv('desafios/desafio_2/road_traffic_deaths_grouped.csv')
# calcular media por matriz


import random
import numpy as np


def calcular_media(variavel):

    matriz = np.array(variavel)

    ones = np.repeat([1], len(matriz))

    # print('Média tradicional: ', matriz.mean())

    matrix_mean = (float((ones @ ones.T)) ** -1) * (matriz @ ones.T)
    resultado = print('Média por matriz: ', np.round(matrix_mean,1))
    
    return(resultado)


calcular_media(df.n_mortes)

def calcular_desvio_padrao(variavel):
    for i in variavel 
