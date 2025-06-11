# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class mySpider_01Item(scrapy.Item):
    # define the fields for your item here like:
    moviename = scrapy.Field()
    movielink = scrapy.Field()
    moviestar = scrapy.Field()


