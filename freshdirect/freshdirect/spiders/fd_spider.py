from __future__ import absolute_import

from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from freshdirect.items import FDItem

class FdSpider(BaseSpider):
	name = "fd"
	allowed_domains = ["freshdirect.com"]
	start_urls = [
		"http://www.freshdirect.com/index.jsp",
		"https://www.freshdirect.com/product.jsp?catId=chclt_bak&productId=pas_chcsfle_frz&variant=feat_pop4&trk=feat&rank=1&impId=1415515303_p1"
	]

	def parse(self, response):
		sel = Selector(response)
		name = sel.xpath("//title/text()").extract()
		url = response.url
		imagePath = sel.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' product-image-container ')]/img/@src").extract()
		price = sel.css("span.productPageSinglePrice::text").extract()
		priceUnit = sel.css("span.productPageSinglePriceUnit::text").extract()
		item = FDItem()
		item['name'] = name
		item['imagePath'] = imagePath
		item['url'] = url
		item['price'] = price
		item['priceUnit'] = priceUnit
		return item