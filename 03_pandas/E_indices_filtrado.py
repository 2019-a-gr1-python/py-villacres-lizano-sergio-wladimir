# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:50:02 2019

@author: Sergio
"""

import pandas as pd


path_guardado = 'C://Users/Sergio/Documents/GitHub/py-villacres-lizano-sergio-wladimir/03_pandas/data/artwork'

df_completo_pickle = pd.read_pickle(path_guardado)

serie_artistas_duplicados = df_completo_pickle['artist']

artistas = pd.unique(serie_artistas_duplicados)

artistas.size

len(artistas)

blake = df_completo_pickle['artist'] == 'Blake, William'

type(blake)  # pandas.core.series.Series

blake.value_counts()

df_blake = df_completo_pickle[blake]

type(df_blake)  # pandas.core.frame.DataFrame
df_blake

