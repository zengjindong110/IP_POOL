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

class IvskyItem(scrapy.Item):
    image_src = scrapy.Field()
    image_name = scrapy.Field()



class A4567kanItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class KuaidailiItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()
    platform = scrapy.Field()




