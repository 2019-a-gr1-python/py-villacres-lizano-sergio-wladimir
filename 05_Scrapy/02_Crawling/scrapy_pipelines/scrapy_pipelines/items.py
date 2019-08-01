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
    regex = r"(\d+\.\d{1,})"
    return float(re.search(regex,text_price).group(0))
        
def get_promedio(promedio_item):
    return promedio_item

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
            ),
        output_processor = TakeFirst()
    )
    titulo = scrapy.Field()
    promedio = scrapy.Field(
        input_processor= MapCompose(
            get_promedio
        ),
        output_processor = TakeFirst() 
    )
    precio = scrapy.Field(
        input_processor= MapCompose(
            get_item_price
        ),
        output_processor = TakeFirst() 
    ) 
    
