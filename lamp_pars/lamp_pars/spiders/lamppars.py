import scrapy


class LampparsSpider(scrapy.Spider):
    name = "lamppars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/kaluga/category/svet"]

    def parse(self, response):
        pass
