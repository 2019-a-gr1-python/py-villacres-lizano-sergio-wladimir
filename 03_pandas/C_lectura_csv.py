# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:57:25 2019

@author: Sergio
"""
import pandas as pd
import os

path='C://Users/Sergio/Documents/GitHub/py-villacres-lizano-sergio-wladimir/03_pandas/data/csv/artwork_data.csv'
pd.read_csv(
        path,
        nrows=5,
        usecols=['id','artist']
        )

columnas_a_usar = ['id','artist','title',
                   'medium','year','acquisitionYear',
                   'height','width','units']

df_completo = pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col='id')

path_guardado = 'C://Users/Sergio/Documents/GitHub/py-villacres-lizano-sergio-wladimir/03_pandas/data/csv/artwork_data.pickle'

df_completo.to_pickle(path_guardado)

df_completo_pickle = pd.read_pickle(path_guardado)

