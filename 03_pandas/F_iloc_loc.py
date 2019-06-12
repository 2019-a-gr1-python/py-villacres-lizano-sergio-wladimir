# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:53:04 2019

@author: Sergio
"""

import pandas as pd


path_guardado = 'C://Users/Sergio/Documents/GitHub/py-villacres-lizano-sergio-wladimir/03_pandas/data/artwork'
df = pd.read_pickle(path_guardado)

primero = df.loc[1035,'artist']
segundo = df.loc[1036,'units']

df.loc[0]  # Error porque no esta dentro del label indice

primero_a = df.iloc[0,1]

primero_b = df.iloc[0,:]

primero_c = df.iloc[0:100,2:4]

tres_primeros = df.head(10)['width'].sort_values(ascending=False).head(3)
tres_ultimos = df.head(10)['width'].sort_values().tail(3)

a = df['year'].sort_values(axis=0)

serie_validado = pd.to_numeric(df['width'], errors='coerce')

df.loc[:,'width'] = serie_validado
df.iloc[:,5] = serie_validado

diez_primeros = df['height'].sort_values(ascending=False).head(10)

diez_ultimos = df['width'].sort_values(ascending=False).tail(10)

serie_validado_height = pd.to_numeric(df['height'], errors='coerce')
df.loc[:,'height'] = serie_validado_height

area = df['height'] * df['width']

type(area)  # Serie

df['area'] = area

df = df.assign(areados = area)

df_area = df['area'].sort_values(ascending=False).head(1)

id_max_area = df['area'].idxmax()  # Label 

id_min_area = df['area'].idxmin()  # Label

registro_mas_area = df.loc[id_max_area]

registro_menor_area = df.loc[id_min_area]