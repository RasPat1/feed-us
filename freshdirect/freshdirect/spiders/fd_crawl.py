# Absolute path needed for this
# http://stackoverflow.com/questions/15991282/unable-to-import-items-in-scrapy
from __future__ import absolute_import

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from freshdirect.items import FDItem

class FdCrawlSpider(CrawlSpider):
    name = 'fd_crawl'
    allowed_domains = ['freshdirect.com']
    start_urls = ['http://www.freshdirect.com/index.jsp']

    rules = (
        # Fresh direct structure 
        # Home => Product 
        # Home => Department => Product
        # Home => Department => Category => Product
        Rule(SgmlLinkExtractor(allow=r'department\.jsp'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'category\.jsp'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'product\.jsp'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        url = response.url
        name = sel.xpath("//title/text()").extract()
        imagePath = sel.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' product-image-container ')]/img/@src").extract()
        price = sel.css("span.productPageSinglePrice::text").extract()
        priceUnit = sel.css("span.productPageSinglePriceUnit::text").extract()
        
        product = FDItem()
        product['name'] = name
        product['imagePath'] = imagePath
        product['url'] = url
        product['price'] = price
        product['priceUnit'] = priceUnit
        return product