import scrapy
from scrapy_pipelines.items import ProductoMercadoLibre
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import re
## deber 

# generar las url 
# anadir el precio (clase, input,output)
# transfromar el precio a float
# exportar a csv
# anadir un pipeline para seleccionar los productos mayores al promedio

def getUrls():
    base_url = 'https://celulares.mercadolibre.com.ec/'
    arreglo_urls = []
    arreglo_urls.append(base_url)
    base_url = 'https://celulares.mercadolibre.com.ec/_Desde_changeThis'
    for url in range(51,1951,50):
        arreglo_urls.append(base_url.replace('changeThis',str(url)))
    return arreglo_urls
class AraniaProductosMercado(scrapy.Spider):
    name = 'arania_mercado_libre'
    
    def start_requests(self):
        urls = getUrls()

        for url in urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):

        productos = response.css('div.item__info')
        for producto in productos:
                # titulo = producto.css('a.name::text')
                # url = producto.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
            producto_loader = ItemLoader(
                item = ProductoMercadoLibre(),
                selector = producto
            )
            
            producto_loader.default_output_processor = TakeFirst()

            producto_loader.add_css(
                'titulo',
                'div>h2.item__title>a.item__info-title>span.main-title::text'
            )
            producto_loader.add_css(
                'precio',
                'div.price__container>div.item__price'
            )
            producto_loader.add_css(
                'vendidos',
                'div.item__stack_column>div.item__stack_column__info>div.stack_column_item>div.item__status>div.item__condition::text'
            )
            producto_loader.add_css(
                'lugar',
                'div.item__stack_column>div.item__stack_column__info>div.stack_column_item>div.item__status>div.item__condition::text'
            )
            yield producto_loader.load_item()
