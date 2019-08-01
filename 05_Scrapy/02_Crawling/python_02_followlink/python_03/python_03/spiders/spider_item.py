import scrapy
from python_03.items import ProductoFybeca
from scrapy.loader import ItemLoader

class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'

    def start_requests(self):
        urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
        ]

        for url in urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):

        productos = response.css('div.product-tile-inner')
        for producto in productos:
            existe_producto = len( producto.css('div.detail'))
            if(existe_producto > 0):
                #titulo = producto.css('a.name::text')
                #url = producto.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
                producto_loader = ItemLoader(
                    item = ProductoFybeca(),
                    selector = producto
                )
                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                ).extract_first()
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )
                yield producto_loader.load_item()
               # print(titulo.extract_first())
               # print(url.extract_first())


        
