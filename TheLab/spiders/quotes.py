from scrapy import Request, Spider


class QuotesSpider(Spider):
    name = 'quotes_crawl'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        i = 1
        while i < 11:
            yield Request(url=self.start_urls[0] + f'page/{i}', callback=self.parse_quotes)
            i += 1

    def parse_quotes(self, response):

        out = {}
        for ele in response.css('.quote'):
            out['author'] = ele.css('.author::text').get()
            out['quote'] = ele.css('.text::text').get()[1:-1]
            out['tags'] = ','.join(ele.css('.tag::text').getall())

            yield out
