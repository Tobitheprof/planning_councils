# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlanningCouncilsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class AdurApplicationItem(scrapy.Item):
   reference = scrapy.Field()
   alt_ref  = scrapy.Field()
   application_received  = scrapy.Field()
   application_validated  = scrapy.Field()
   address = scrapy.Field()
   proposal = scrapy.Field()
   status = scrapy.Field()
   appeal_status = scrapy.Field()
   appeal_decision = scrapy.Field()
   cases = scrapy.Field()
   documents = scrapy.Field()
   property = scrapy.Field()


class AylesburyApplicationItem(scrapy.Item):
    reference = scrapy.Field()
    application_validated = scrapy.Field()
    address = scrapy.Field()
    proposal = scrapy.Field()
    status = scrapy.Field()
    appeal_status = scrapy.Field()
    appeal_decision = scrapy.Field()
    documents = scrapy.Field()
    cases = scrapy.Field()
    property = scrapy.Field()

class BasildonBoroughApplicationItem(scrapy.Item):
   reference = scrapy.Field()
   alt_ref  = scrapy.Field()
   application_received  = scrapy.Field()
   application_validated  = scrapy.Field()
   address = scrapy.Field()
   proposal = scrapy.Field()
   status = scrapy.Field()
   appeal_status = scrapy.Field()
   appeal_decision = scrapy.Field()
   cases = scrapy.Field()
   documents = scrapy.Field()
   property = scrapy.Field()