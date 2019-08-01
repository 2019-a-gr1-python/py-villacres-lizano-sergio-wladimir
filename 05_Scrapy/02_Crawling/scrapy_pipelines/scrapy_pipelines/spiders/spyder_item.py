import scrapy
from scrapy_pipelines.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import re
## deber 

# generar las url 
# anadir el precio (clase, input,output)
# transfromar el precio a float
# exportar a csv
# anadir un pipeline para seleccionar los productos mayores al promedio
def get_urls():
    base_url = 'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=changeThis&pp=25'
    return [base_url.replace('changeThis',str(url)) for url in range(0,176,25)]
    #for page in range(0,176,25):
        



class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'

    def start_requests(self):
        #urls = [
        #'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=25&pp=25'
        #]
        urls = get_urls() 

        for url in urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):

        productos = response.css('div.product-tile-inner')
        promedio = 0.0
        num_items = 0
        for prod in productos:
            text_price = prod.css('.price::attr(data-bind)')
            precio = str(text_price).replace(").formatMoney(2, '.', '\">]","").replace(").formatMoney(2, '.', ',\">]","").replace("[<Selector xpath=\"descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' price ')]/@data-bind\" data=\"text:'$' + (","")
            try:
                promedio = promedio + float(precio)
                num_items = num_items +1
            except:
                print(precio)

        for producto in productos:
            existe_producto = len( producto.css('div.detail'))
            if(existe_producto > 0):
                # titulo = producto.css('a.name::text')
                # url = producto.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
                producto_loader = ItemLoader(
                    item = ProductoFybeca(),
                    selector = producto
                )
                
                producto_loader.default_output_processor = TakeFirst()

                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                    )
                
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )
                producto_loader.add_value(
                    'promedio',
                    promedio/num_items
                )

                producto_loader.add_css(
                    'precio',
                    '.price::attr(data-bind)'
                )

                #producto_imprimir = producto_loader.load_item()
                #print(producto_imprimir)
                yield producto_loader.load_item()
