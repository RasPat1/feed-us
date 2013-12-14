# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FreshdirectItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    image = Field()
    link = Field()
    price = Field()
    about = Field()
    nutrition = Field()
    qualityRating = Field()
    pass
