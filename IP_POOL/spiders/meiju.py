import scrapy
from IP_POOL.items import IpPoolItem
from scrapy import cmdline,Spider


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.tv/alltop_hit.html']

    def parse(self, response):
        movies =  response.xpath("//ul[@class='top-list fn-clear']/li")
        print(movies)
        for movie in movies:

            item = IpPoolItem()

            item["name"] = movie.xpath("./h5/a/@title").extract()[0]
            item["href"] = movie.xpath("./h5/a/@href").extract()[0]

            yield item

if __name__ == '__main__':
    cmdline.execute("scrapy crawl meiju --nolog".split())
