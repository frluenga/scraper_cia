from gc import callbacks
from os import link
import scrapy

## links = '//div[@class="content"]//li[@class="leaf"]/a/@href'
# title = //li[@class="leaf active-trail"]/a/text()
# Body = //div[@class="content clearfix"]//p[3]/text()

class Cia(scrapy.Spider):
    name = 'cia'
    start_urls = ['https://www.cia.gov/readingroom/historical-collections']
    custom_settings = {
        'FEED_URI' : 'cia.csv',
        'FEED_FORMAT':'csv',
        'FEED_EXPORT_ENCODING':'utf-8'  
    }


    def parse(self,response):
        links_desclassified = response.xpath('//div[@class="content"]//li[@class="leaf"]/a/@href').getall()
        # Recorrer todos los links para extraer la información.
        for link in links_desclassified:
            yield response.follow(link,callback=self.parse_link,cb_kwargs= {
                                                                            'url':response.urljoin(link)            
                                                                            })


    def parse_link(self,response,**kwargs):
        link = kwargs['url']
        title = response.xpath('//li[@class="leaf active-trail"]/a/text()').get()
        
        
        yield {
            'url':link,
            'title':title
        }