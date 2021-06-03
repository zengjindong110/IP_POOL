import scrapy
from scrapy import cmdline, Spider


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.k8jds.com/index.php/vod/show/class/%E5%96%9C%E5%89%A7/id/20/page/1.html',
    ]

    def parse(self, response):
        movies = response.xpath("//div[@class='stui-vodlist__detail']")
        for movie in movies:
            movie_name = movie.xpath("./h4/a/text()").get()
            print(movie_name)
            movie_url = movie.xpath("./h4/a/@href").get()
            yield {"name": movie_name}

        next_page = movie_url
        if next_page is not None:

            next_page = response.urljoin("https://www.k8jds.com"+next_page)
            yield scrapy.Request(next_page, callback=self.parse)


if __name__ == '__main__':
    cmdline.execute("scrapy crawl quotes --nolog".split())
