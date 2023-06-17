import scrapy
from urllib.parse import urljoin
from planning_councils.items import AylesburyApplicationItem

class PlanningSpider(scrapy.Spider):
    name = "aylesbury_council"
    allowed_domains = ["pa.chilternandsouthbucks.gov.uk"]

    def start_requests(self):
        url = "https://pa.chilternandsouthbucks.gov.uk/online-applications/search.do?action=weeklyList&searchType=Application"
        yield scrapy.Request(url=url, callback=self.submit_form)

    
    def submit_form(self, response):
        token = response.css('input[name="_csrf"]::attr(value)').extract_first()
        week_beginning = response.css("select#week option::text").get()
        data = {
            '_csrf' : token,
            'week' : week_beginning,
            #ddmmyy
        }
        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_results_page, dont_filter=True)

    def parse_results_page(self, response):
        application = response.xpath("//ul[@id='searchresults']/li")

        for item in application:
            relative_url = item.xpath("a/@href").get()
            absolute_url = urljoin(response.url, relative_url)
            yield response.follow(absolute_url, callback=self.parse_details_page)

        next_page_url = response.xpath("//a[contains(text(), 'Next')]/@href").get()
        if next_page_url:
            next_page_url = urljoin(response.url, next_page_url)
            yield response.follow(next_page_url, callback=self.parse_results_page)

    def parse_details_page(self, response):
        application_item = AylesburyApplicationItem()

        table_rows = response.css("table tr") # Setting table rows as root executioner


        application_item['reference'] = table_rows[0].css("td ::text").get()
        application_item['application_validated'] = table_rows[1].css("td ::text").get()
        application_item['address'] = table_rows[2].css("td ::text").get()
        application_item['proposal'] = table_rows[3].css('td ::text').get()
        application_item['status'] = response.css(".caseDetailsStatus::text").get()
        application_item['appeal_status'] = table_rows[5].css('td ::text').get()
        application_item['appeal_decision'] = table_rows[6].css('td ::text').get()
        application_item['documents'] = "https://pa.chilternandsouthbucks.gov.uk" + str(response.css('p.associateddocument a::attr(href)').get())
        application_item['cases'] = "https://pa.chilternandsouthbucks.gov.uk" + str(response.css("p.associatedcase a::attr(href)").get())
        application_item['property'] = "https://pa.chilternandsouthbucks.gov.uk" + str(response.css("p.associatedproperty a::attr(href)").get())


        yield application_item
