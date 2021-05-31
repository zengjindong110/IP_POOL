import scrapy
from scrapy import cmdline, Spider
from IP_POOL.items import DuanziItem


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['duanziwang.com']
    start_urls = ['https://www.duanziwang.com/t/57uP5YW456yR6K%2Bd_1.html']
    url = "https://www.duanziwang.com/t/57uP5YW456yR6K%2Bd_{}.html"
    num = 2

    def parse(self, response):
        duanzis = response.xpath("//div[@class='nr']/dl")

        for duanzi in duanzis:
            item = DuanziItem()
            item["title"] = duanzi.xpath("./span/dd/a/strong/text()").extract()[0]
            item["content"] = duanzi.xpath("./dd/text()").extract()[0]
            print(item)
            yield item
        if self.num < 10:
            request_url = self.url.format(str(self.num))
            print(request_url)
            self.num += 1
            yield scrapy.Request(url=request_url, callback=self.parse)


if __name__ == '__main__':
    cmdline.execute("scrapy crawl duanzi --nolog".split())
