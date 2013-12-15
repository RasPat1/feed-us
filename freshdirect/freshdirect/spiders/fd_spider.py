from scrapy.spider import BaseSpider

class FdSpider(BaseSpider):
	name = "fd"
	allowed_domains = ["freshdirect.com"]
	start_urls = [
		"http://www.freshdirect.com/"
	]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		open(filename, 'wb').write(response.body)
