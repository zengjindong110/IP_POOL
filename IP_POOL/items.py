# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IpPoolItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    href = scrapy.Field()
    # pass


class DuanziItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()



class A4567kanItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

