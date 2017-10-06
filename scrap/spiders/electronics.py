# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrap.items import ScrapItem

class ElectronicsSpider(CrawlSpider):
    name = 'electronics'
    allowed_domains = ['example.com']
    start_urls = [
        'http://example.com/page',
        ]
    rules = (Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)), callback="parse_item", follow=True),)    

    def parse_item(self, response):
        print('Processing..' + response.url)
        item_links = response.css('.normal > .detailsLink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        price = response.css('.pricelabel > strong > span::text').extract()[0]
        url   = response.url
        place = response.css('.cpointer > strong > a::text').extract()[0]
        device = response.css('.brlefte5 > a > span::text').extract()[0]
        idiklan = response.css('.brlefte5 > span > span.inlblk::text').extract()[0]
        category = response.css('div.clr.offerheadinner.pding15.pdingright20 > p > label::text').extract()[0]
        dilihat =  response.css('#offerbottombar > div > strong::text').extract()[0]

        item = ScrapItem()
        item['title'] = title
        item['price'] = price 
        item['url'] = url   
        item['place'] = place 
        item['device'] = device 
        item['idiklan'] = idiklan 
        item['category'] = category 
        item['dilihat'] = dilihat 
        yield item
