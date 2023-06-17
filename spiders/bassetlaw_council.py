import scrapy


class BassetlawCouncilSpider(scrapy.Spider):
    name = "bassetlaw_council"
    allowed_domains = ["publicaccess.bassetlaw.gov.uk"]
    start_urls = ["https://publicaccess.bassetlaw.gov.uk"]

    def parse(self, response):
        pass
