# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ComicspiderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    link = Field()
    desc = Field()
    content = Field()
    episode_number = Field()
    image_urls = Field()
    images = Field()
    meta = Field()
    created_at = Field()
    category = Field()
    post_type = Field()
    soft_delete = Field()
    
    pass
