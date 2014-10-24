# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

# Let's ensure that we got only one value back in each list
# Convert the list to just a string
# That there is no white space charactrers
# urls are not lists but simply strings
class SanitizePipeline(object):
	def process_item(self, item, spider):
		for field in item:
			if len(item[field]) is not 1:
				raise DropItem('too many vals')

			item[field] = ''.join(item[field])
			item[field] = item[field].strip(' \t\n\r')
			if len(item[field]) is 0:
				DropItem('empty field')
		if not item['title']:
			raise DropItem('no name')
		return item

class DuplicatePipeline(object):
	def __init__(self):
		self.titles_seen = set()
	def process_item(self, item, spider):
		if (item['title']) in self.titles_seen:
			raise DropItem('duplicate')
		else:
			self.titles_seen.add((item['title']))
			return item
