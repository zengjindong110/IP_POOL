import scrapy


class A4567kanSpider(scrapy.Spider):
    name = '4567kan'
    allowed_domains = ['www.4567kan.com']
    start_urls = ['http://www.4567kan.com/']

    def parse(self, response):
        pass
