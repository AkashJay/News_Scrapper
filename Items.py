import scrapy as scrapy


class NewsItem(scrapy.Item):
    id = scrapy.Field()
    heading = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()

