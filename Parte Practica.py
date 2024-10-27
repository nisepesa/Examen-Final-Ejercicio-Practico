# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:37:07 2024

@author: PC
"""

import pandas as pd
import matplotlib.pyplot as plt


datos= pd.read_csv('living.csv')
print(datos.head())  
print(datos.describe())  


'''Numero de filas y columnas'''
numero_filas, numero_columnas = datos.shape
print("Número de filas:", numero_filas)
print("Número de columnas:", numero_columnas)



'''Costo de vida promedio'''
costo_v_promedio = datos['Cost of living, 2017'].mean()
print("Costo de vida promedio:", costo_v_promedio)


''''País con el costo de vida más alto y más bajo'''
pais_costo_mas_alto = datos.loc[datos['Cost of living, 2017'].idxmax()]['Countries']
pais_costo_mas_bajo = datos.loc[datos['Cost of living, 2017'].idxmin()]['Countries']
print("País con el costo de vida más alto:", pais_costo_mas_alto)
print("País con el costo de vida más bajo:", pais_costo_mas_bajo)