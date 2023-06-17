import scrapy


class BathAndNorthEasstSoomersetCouncilSpider(scrapy.Spider):
    name = "bath_and_north_easst_soomerset_council"
    allowed_domains = ["bathnes.gov.uk"]
    start_urls = ["https://bathnes.gov.uk"]

    def parse(self, response):
        pass
