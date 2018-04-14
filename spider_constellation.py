import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://cstrecords.com/artists/']

    def parse(self, response):
        for artist in response.css('div#activeartists h5 a'):
            yield {'artist': link.css('a ::text').extract_first()}

