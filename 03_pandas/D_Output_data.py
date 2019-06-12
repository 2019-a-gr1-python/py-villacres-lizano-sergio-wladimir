# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 08:09:55 2019

@author: Sergio
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = '/Users/usrdel/Documents/GitHub/py-eguez-sarzosa-vicente-adrian/03_Pandas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

df = df_completo_pickle.iloc[49980:50019,:].copy()


#  Tipos de archivos 
#  
#  - JSON
#  - SQL
#  - EXCEL


######################## Excel ##########################

df.to_excel('ejemplo_basico.xlsx')

df.to_excel('ejemplo_basico_sin_indices.xlsx', index = False)

columnas = ['artist','title','year']

df.to_excel('columnas.xlsx', columns = columnas)


# Multiples hojas de trabajos (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')

df.to_excel(writer, sheet_name = 'Preview Dos', index=False)

df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()

# Formateo Condicional

artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': '2_color_scale',
        'min_value': '10',
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile'
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()