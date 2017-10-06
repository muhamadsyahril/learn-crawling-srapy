# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    url   = scrapy.Field()
    place = scrapy.Field()
    device = scrapy.Field()
    idiklan = scrapy.Field()
    category = scrapy.Field()
    dilihat = scrapy.Field()
