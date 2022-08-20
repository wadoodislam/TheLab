from scrapy import Request, Spider


class CASpider(Spider):
    name = 'ca_crawl'
    allowed_domains = ['ca-sports.com.pk']
    start_urls = ['https://www.ca-sports.com.pk/']

    def parse(self, response):
        for links in response.css('.container .partition2 a::attr(href)').getall():
            yield Request(url=response.urljoin(links), callback=self.parse_category)

    def parse_category(self, response):
        for i in range(1, len(response.css('.pagination li a ::attr(href)').getall()) - 1):
            yield Request(url=response.url + f"?page={i}", callback=self.parse_pagination)

    def parse_pagination(self, response):
        for product_link in response.css('.product-box .front a::attr(href)').getall():
            yield Request(url=product_link, callback=self.parse_product, meta={'aliyan': 1})

    def parse_product(self, response):
        item = {
            'title': response.css('.product-right h1::text').get(),
            'price': response.css('.product-right h3::text').get(),
            'product-details': "\n".join(response.css('.product-des ::text').getall()[1:]),
            'available-Colors': response.css('.product-title:contains("Colors") + ul img::attr(src)').getall(),
            'sizes': response.css('.product-title:contains("sizes") + .size-box li span::text').getall(),
            'images': [x for x in response.css('.img-fluid::attr(src)').getall() if  not x.__contains__("icon")]
        }
        yield item
        if not response.meta.get('parsing_variation'):
            if len(item['available-Colors']) > 1:
                for available_color in [x for x in response.css('.product-title + ul a::attr(href)').getall() if x != response.url]:
                    yield Request(url=available_color, callback=self.parse_product, meta={'parsing_variation': True})
