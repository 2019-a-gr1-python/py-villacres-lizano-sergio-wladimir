import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'libros_mis'  # Heredado (conservar nombre)
    
    allowed_domains = [  # Heredado (conservar nombre)
        'books.toscrape.com'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'http://books.toscrape.com/'
    ]
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
                allow=('catalogue/category/books/mystery_3/','catalogue/category/books/fantasy_19/'),
            ), callback='parse_page')
        ,
    )


    rules = regla_tres


    def parse_page(self, response):
        lista_programas = response.css('article.product_pod>h3>a::attr(title)').extract()

        for agencia in lista_programas:
            with open('misterio_fantasia.txt', 'a+') as archivo:
                archivo.write(agencia + '\n')