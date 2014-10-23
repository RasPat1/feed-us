# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from freshdirect_pdp.items import FreshdirectPdpItem 

class FdSpider(CrawlSpider):
    name = "fd"
    allowed_domains = ["freshdirect.com"]
    start_urls = (
        'http://www.freshdirect.com/',
    )
    rules = (
    Rule(LinkExtractor(allow=('browse\.jsp', ))),
	Rule(LinkExtractor(allow=('pdp\.jsp', )), callback='parse_item'),
	)

    def parse_item(self, response):
    	item = FreshdirectPdpItem()
    	item['title'] = response.css('h1.pdpTitle::text').extract()
    	item['price'] = response.css('div.pdp-price::text').extract()
    	item['image'] = response.css('div.main-image img::attr(src)').extract()
    	return item

