import scrapy as scrapy


class NewsItem(scrapy.Item):
    id = scrapy.field()
    heading = scrapy.field()
    content = scrapy.field()
    date = scrapy.field()

