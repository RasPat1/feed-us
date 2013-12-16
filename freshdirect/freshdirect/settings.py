# Scrapy settings for freshdirect project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

# BOT_NAME = 'freshdirect'
# BOT_VERSION = '1.0'

SPIDER_MODULES = ['freshdirect.spiders']
NEWSPIDER_MODULE = 'freshdirect.spiders'
DEFAULT_ITEM_CLASS = 'freshdirect.items.FDItem'
# USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

