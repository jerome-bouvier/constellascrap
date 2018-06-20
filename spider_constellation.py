import scrapy

class BlogSpider(scrapy.Spider):
    name = 'constellation_spider'
    start_urls = ['http://cstrecords.com/artists/']

    def parse(self, response):
        for link in response.css('div#activeartists h5 a'):
            yield {'artist': link.css('a ::text').extract_first()}

