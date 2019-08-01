# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

class FiltrarPrecios(object):
    def process_item(self, item, spider):
        if(float(item['precio']) > 100):
            return item
        else:
            raise DropItem(item['titulo'])

class FiltrarMayoresPromedio(object):
    def process_item(self,item,spider):
        if(item['precio']>item['promedio']):
            return item
        else:
            raise DropItem(item['titulo'])



