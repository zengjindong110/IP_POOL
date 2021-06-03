import scrapy
from IP_POOL.items import A4567kanItem
from scrapy import cmdline, Spider


class A4567kanSpider(scrapy.Spider):
    name = '4567kan'
    # allowed_domains = ['www.4567kan.com']
    start_urls = ['https://www.k8jds.com/index.php/vod/show/class/%E5%96%9C%E5%89%A7/id/1.html']
    url = "https://www.k8jds.com/index.php/vod/show/class/%E5%96%9C%E5%89%A7/id/20/page/{}.html"
    page = 2

    def parse(self, response):
        movies = response.xpath("//div[@class='stui-vodlist__detail']")
        for movie in movies:
            movie_name = movie.xpath("./h4/a/text()").get()
            item = A4567kanItem()
            item["title"] = movie_name
            movie_url = movie.xpath("./h4/a/@href").get()
            yield scrapy.Request(url="https://www.k8jds.com" + movie_url, callback=self.parse_content,
                                 meta={"item": item})

        # if self.page < 100:
        if movie_url is not None:
            # res_url = self.url.format(str(self.page))
            # self.page += 1
            # yield scrapy.Request(url=res_url, callback=self.parse)
            yield response.follow(movie_url,callback=self.parse)

    def parse_content(self, response):
        item = response.meta["item"]
        movie_content = response.xpath("//span[@class='detail-content']/text()").get()
        item["content"] = movie_content
        print(item)
        yield item


if __name__ == '__main__':
    cmdline.execute("scrapy crawl 4567kan --nolog".split())
