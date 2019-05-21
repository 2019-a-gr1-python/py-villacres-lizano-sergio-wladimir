# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:26:31 2019

@author: Sergio
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = ((1,2,3,4))
np_numeros = np.array(3)
numeros_serie_a = pd.Series(lista_numeros)
numeros_serie_b = pd.Series(tupla_numeros)
numeros_serie_c = pd.Series(np_numeros)
numeros_serie_d = pd.Series(lista_numeros)
numeros_serie_e = pd.Series([
        4,
        (),
        [],
        "Sergio",
        {"nombre":"Sergio"}
        ])

numeros_serie_a[0]
lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]
serie_ciudades = pd.Series(lista_ciudades,index=["A","C","L","Q"])

serie_ciudades["A"]

serie_ciudades[0]

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Loja":4000
        }

serie_valor_ciudad = pd.Series(valores_ciudad)
type(serie_valor_ciudad)
serie_valor_ciudad

ciudades_menores_5000 = serie_valor_ciudad == 8750

serie_menor_5000 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Cuenca"] = 8750

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)

np.square(serie_valor_ciudad)
np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
            "Quito":1500,
            "Loja":4000,
            "Guayaquil":2000
        })

ciudades_dos = pd.Series({
            "Montañita":300,
            "Guayaquil":10000,
            "Quito":2000
        })
ciudades_tres = pd.Series({
            "Montañita":300,
        })

print(ciudades_uno * ciudades_dos)

randomico = np.random.rand(3)
serie_tres_rand = pd.Series(randomico)


ciudades_uno.index

ciudades_uno.add(ciudades_tres)
ciudades_uno.append(ciudades_tres)
ciudades_uno.append(ciudades_dos)
ciudades_uno.add(ciudades_dos)
pd.concat([ciudades_uno,ciudades_dos])
ciudades_uno.max()
ciudades_uno.min()

ciudades_uno.head(2)
ciudades_uno.tail(2)
ciudades_uno.sortlevel()
ciudades_uno.sort_values(ascending = False).head(2)
ciudades_uno.sort_values(ascending = False).tail(2)
ciudades_uno.where(ciudades_uno>1000,ciudades_uno*1.05)
ciudades_uno.map(format*1.05)
def calculo(valor):
    if(valor<=1000):
        return valor * 1.05
    if(valor>1000 and valor <= 10000):
        return valor * 1.10
    if(valor > 10000):
        return valor * 1.15
    

    

ciudades_uno.where(ciudades_uno < 2000)

ciudades_uno.T
ciudades_uno.iat














