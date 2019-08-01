# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
import re 

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    return texto.replace(cadena_a_reemplazar,url)

def get_item_price(text_price):
    text=str(text_price)
    print(text+'HOLA')
    return text.replace('<div class="item__price "> <span class="price__symbol">U$S</span> <span class="price__fraction">','').replace('</span></div>','').replace('</span> <span class="price__decimals">','.')

def get_nombre_producto(producto_nombre):
    texto = str(producto_nombre)
    texto = texto.lower()
    retorno = 'Otro'
    if texto.find("samsung") > 0:
        retorno = 'Samsung'
    elif texto.find("xiaomi") > 0:
        retorno = 'Xiaomi'
    elif texto.find("motorola") > 0:
        retorno = 'Motorola'
    elif texto.find("huawei") > 0:
        retorno = 'Huawei'
    elif texto.find("iphone") > 0:
        retorno = 'iPhone'
    elif texto.find("sony xperia") > 0:
        retorno = 'Sony Xperia'
    return retorno

def obtenerVentas(vendidos):
    text_vendidos = str(vendidos)
    if text_vendidos.find("-") > 0:
        text_vendidos= text_vendidos[0:text_vendidos.find("-")]
        if text_vendidos.find("vendido") > 0:
            text_vendidos= text_vendidos.replace(' ','').replace('vendidos','').replace('vendido','')
        else:
            text_vendidos = 0
    else:
        if text_vendidos.find("vendido") > 0:
            text_vendidos= text_vendidos.replace(' ','').replace('vendidos','').replace('vendido','')
        else:
            text_vendidos = 0
    return text_vendidos

def obtenerUbicacion(ubicacion):
    text_ubicacion = str(ubicacion)
    if text_ubicacion.find("-")>0:
        if text_ubicacion.find("vendidos") > 0:
            text_ubicacion= text_ubicacion[text_ubicacion.find("vendidos")+10:len(text_ubicacion)].replace(' ','')
        elif text_ubicacion.find("vendido") > 0:
            text_ubicacion=text_ubicacion[text_ubicacion.find("vendido")+9:len(text_ubicacion)]
        else:
            text_ubicacion='No especifica'
    else:
        if text_ubicacion.find("vendidos") > 0:
            text_ubicacion= text_ubicacion[text_ubicacion.find("vendidos")+10:len(text_ubicacion)].replace(' ','')
        elif text_ubicacion.find("vendido") > 0:
            text_ubicacion=text_ubicacion[text_ubicacion.find("vendido")+9:len(text_ubicacion)]
        else:
            text_ubicacion='No especifica'

    if len(text_ubicacion.replace(' ',''))<1:
        text_ubicacion='No especifica'
    elif len(text_ubicacion)<=0:
        text_ubicacion='No especifica'

    
    return text_ubicacion

class ProductoMercadoLibre(scrapy.Item):
    titulo = scrapy.Field(
        input_processor= MapCompose(
            get_nombre_producto
        ),
        output_processor = TakeFirst() 
    )
    vendidos = scrapy.Field(
        input_processor= MapCompose(
            obtenerVentas
        ),
        output_processor = TakeFirst() 
    )
    lugar = scrapy.Field(
        input_processor= MapCompose(
            obtenerUbicacion
        ),
        output_processor = TakeFirst() 
    )
    precio = scrapy.Field(
        input_processor= MapCompose(
            get_item_price
        ),
        output_processor = TakeFirst() 
    )
    
