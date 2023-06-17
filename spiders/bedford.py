import scrapy


class BedfordSpider(scrapy.Spider):
    name = "bedford"
    allowed_domains = ["gggg.url"]
    start_urls = ["https://gggg.url"]

    def parse(self, response):
        pass
