import scrapy
from scrapy import cmdline, Spider
from IP_POOL.items import KuaidailiItem


class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidiali.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    def parse(self, response):

        ips = response.xpath("//table[@class='table table-bordered table-striped']/tbody/tr")
        item = KuaidailiItem()

        for ip in ips:
            item["ip"] = ip.xpath("./td[1]/text()").get()
            item["port"] = ip.xpath("./td[2]/text()").get()
            item["type"] = ip.xpath("./td[4]/text()").get()
            item["platform"] = self.name
            print(item)
            yield item


if __name__ == '__main__':
    cmdline.execute("scrapy crawl kuaidaili --nolog".split())
