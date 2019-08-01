import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
def getUrls():
    base_url = 'https://celulares.mercadolibre.com.ec/'
    arreglo_urls = []
    arreglo_urls.append(base_url)
    base_url = 'https://celulares.mercadolibre.com.ec/_Desde_changeThis'
    for url in range(51,1951,50):
        arreglo_urls.append(base_url.replace('changeThis',str(url)))
        print(url)
    return arreglo_urls
class AraniaCrawlOnu(CrawlSpider):
    name = 'libros_mis'  # Heredado (conservar nombre)
    
    allowed_domains = [  # Heredado (conservar nombre)
        'celulares.mercadolibre.com.ec'
    ]
     start_urls = getUrls() #[  # Heredado (conservar nombre)
    #     'https://celulares.mercadolibre.com.ec/'
    # ]
    # Heredado (conservar nombre)

    regla_uno = (
        Rule(LinkExtractor(), callback='parse_page')
        ,
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=('funds-programmes-specialized-agencies-and-others')
            ), callback='parse_page')
        ,
    )
    
    url_segmento_restringido = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=('_ItemTypeID_N'),
            ), callback='parse_page')
        ,
    )


    rules = regla_tres


    def parse_page(self, response):
        lista_programas = response.css('div.item__info-container.highlighted>div>h2>a>span.main-title::text').extract()

        for agencia in lista_programas:
            with open('productos.txt', 'a+') as archivo:
                archivo.write(agencia + '\n')