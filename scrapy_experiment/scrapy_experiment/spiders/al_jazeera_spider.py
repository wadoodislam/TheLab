import json

import scrapy
import logging

from ..items import ScrapyExperimentItem


class AljazeeraSpider(scrapy.Spider):
    offset_value = 0
    name = 'al_jazeera'
    url_t = 'https://www.aljazeera.com/graphql?wp-site=aje&operationName=AjeSectionPostsQuery&variables=%7B%22category%22%3A%22news%22%2C%22categoryType%22%3A%22categories%22%2C%22postTypes%22%3A%5B%22blog%22%2C%22episode%22%2C%22opinion%22%2C%22post%22%2C%22video%22%2C%22external-article%22%2C%22gallery%22%5D%2C%22quantity%22%3A10%2C%22offset%22%3A{}%7D&extensions=%7B%7D'

    start_urls = [url_t.format(offset_value)]

    def parse(self, response):
        logging.getLogger().setLevel(logging.INFO)
        json_response = json.loads(response.text)
        article_item = ScrapyExperimentItem()

        for article in json_response['data']['articles']:
            article_item['title'] = article['title']
            article_item['date'] = article['date']
            article_item['breaking_news'] = article['isBreaking']
            article_item['url'] = article['shortUrl']
            article_item['author'] = article['author']
            # author =  [data if article['author'][0]['name'] else None]

            yield article_item
        self.offset_value = self.offset_value + 10
        next_page = self.url_t.format(self.offset_value)
        if self.offset_value < 1000:
            yield response.follow(next_page, callback=self.parse)
