# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class NamePipeline(object):
    def process_item(self, item, spider):
        name = item.get('name')[0]
        if name:
            name = name.partition("-")
            if name[2]:
                item['name'] = name[2].strip()
            else:
                raise DropItem()
            return item
        else:
            raise DropItem()