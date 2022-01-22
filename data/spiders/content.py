import scrapy

class Content(scrapy.Spider):
    name = 'content'
    start_urls = ['https://www.cia.gov/readingroom/collection/aquiline']

    def parse(self,response):
        with open('./content_of_two_link.html','w',encoding='utf-8') as f:
            f.write(response.text)


