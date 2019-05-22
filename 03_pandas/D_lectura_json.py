# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:34:27 2019

@author: Sergio
"""

import json
import pandas as pd
import os

path='C://Users/Sergio/Documents/GitHub/py-villacres-lizano-sergio-wladimir/03_pandas/data/artwork'

archivo='/a/000/a00001-1035.json'
path_archivo = path+archivo
llaves = ['id','all_artists',
          'title','medium',
          'dateText','acquisitionYear',
          'height','width','units']

with open(path_archivo) as texto_json:
    contenido_json = json.load(texto_json)
    print(type(contenido_json))
    print(contenido_json)
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    registro_df_tupla = tuple(registro_df_lista)

print(registro_df_tupla)
df_chiquito = pd.DataFrame([registro_df_lista])
df_chiquito_t = pd.DataFrame([registro_df_tupla])

   
leer_json(path_archivo,llaves)