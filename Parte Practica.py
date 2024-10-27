# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:37:07 2024

@author: PC
"""

import pandas as pd
import matplotlib.pyplot as plt

#-------------------------------------------------------------------
datos= pd.read_csv('living.csv')
print(datos.head())  
print(datos.describe())  


'''Numero de filas y columnas'''
numero_filas, numero_columnas = datos.shape
print("Número de filas:", numero_filas)
print("Número de columnas:", numero_columnas)



'''Costo de vida promedio'''
costo_v_promedio = datos['Cost of living, 2017'].mean().round(2)
print("Costo de vida promedio:", costo_v_promedio)



''''País con el costo de vida más alto y más bajo'''
pais_costo_mas_alto = datos.loc[datos['Cost of living, 2017'].idxmax()]['Countries']
pais_costo_mas_bajo = datos.loc[datos['Cost of living, 2017'].idxmin()]['Countries']
print("País con el costo de vida más alto:", pais_costo_mas_alto)
print("País con el costo de vida más bajo:", pais_costo_mas_bajo)



'''Costo de vida y ranking de Perú (si existe en el dataset)'''
if 'Peru' in datos['Countries'].values:
    costo_peru = datos.loc[datos['Countries'] == 'Peru', 'Cost of living, 2017'].values[0]
    ranking_peru = datos.loc[datos['Countries'] == 'Peru', 'Global rank'].values[0]
    print("Costo de vida en Perú:", costo_peru)
    print("Ranking de Perú:", ranking_peru)
    
#------------------------------------------------------------------

''''Los 10 países con el costo de vida más alto'''
top_10_costo_alto = datos.nlargest(10, 'Cost of living, 2017')
plt.figure(figsize=(10, 6))
plt.barh(top_10_costo_alto['Countries'], top_10_costo_alto['Cost of living, 2017'])
plt.xlabel('Costo de Vida')
plt.title('Los 10 Países con el Costo de Vida Más Alto')
plt.gca().invert_yaxis()
plt.show()



''''Los 10 países con el costo de vida más bajo'''
top_10_costo_bajo = datos.nsmallest(10, 'Cost of living, 2017')
plt.figure(figsize=(10, 6))
plt.barh(top_10_costo_bajo['Countries'], top_10_costo_bajo['Cost of living, 2017'])
plt.xlabel('Costo de Vida')
plt.title('Los 10 Países con el Costo de Vida Más Bajo')
plt.gca().invert_yaxis()
plt.show()

'''Costo de vida en los países de América'''
paises_america = datos[datos['Continent'] == 'America']
plt.figure(figsize=(12, 8))
plt.barh(paises_america['Countries'], paises_america['Cost of living, 2017'])
plt.xlabel('Costo de Vida')
plt.title('Costo de Vida en Países de América')
plt.gca().invert_yaxis()
plt.show()


