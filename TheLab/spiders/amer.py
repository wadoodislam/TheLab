from scrapy import Request, Spider


class sportsSpider(Spider):
    name = 'sports_crawl'
    allowed_domains = ['amerislam.com']
    start_urls = ['https://amerislam.com/']

    def parse(self, response):
        for ele in response.css('.collection-list .card__heading a::attr(href)').getall():
            yield Request(url=response.urljoin(ele), callback=self.parse_category)

    def parse_category(self, response):
        for ele in response.css('.card__inner h3 a::attr(href)').getall():
            yield Request(url=response.urljoin(ele), callback=self.parse_item)

    def parse_item(self, response):
        item = {
            'price': response.css('.price__regular .price-item::text').get().strip(),
            'description': [i.strip() for i in response.css('.product__description ::text').getall() if i.strip() is not  "" ]
        }
        response

        yield item
