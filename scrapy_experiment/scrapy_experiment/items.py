# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyExperimentItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    breaking_news = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
