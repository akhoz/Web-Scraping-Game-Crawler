# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GamecrawlerItem(scrapy.Item):
    # items fiels
    game_name = scrapy.Field()
    game_price = scrapy.Field()
    game_rating = scrapy.Field()
    game_hours = scrapy.Field()
