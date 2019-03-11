import scrapy
import logging

logging.getLogger('scrapy').setLevel(logging.WARNING)


class BlogSpider(scrapy.Spider):
    name = 'constellation_spider'
    start_urls = ['http://cstrecords.com/artists/']

    def parse(self, response):
        links = response.css('div#activeartists h5 a::attr(href)')
        for link in links:
            yield response.follow(url=link, callback=self.parse_artist)

    def parse_artist(self, response):
        artist_name = response.css(
            'div#sac_top ::text').extract_first().strip()
        artist_news = response.css(
            'div.newstitle > a ::text').extract_first().strip()
        disco = response.css(
            'span.smallrname ::text')
        artist_release = [r.strip() for r in disco.extract()]
        yield {'artist': artist_name,
               'release':  artist_release,
               'last news': artist_news
               }
