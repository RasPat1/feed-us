# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FDItem(Item):
    # define the fields for your item here like:
    name = Field()
    imagePath = Field()
    url = Field()
    price = Field()
    priceUnit = Field()
    about = Field()
    nutrition = Field()
    qualityRating = Field()
    pass
