import scrapy
import json
from games import allowed_games
import os

class InstantGamingSpider(scrapy.Spider):
    name = "InstantGaming" # Name of the Spider
    start_urls = ["https://www.instant-gaming.com/en/search/"] # Starting url
    page = 1 # IDX of the page

    def __init__(self):
        self.games = []
        self.game_list = []
        self.allowed_games = set()

    def check_cheepest_price(self, game):
        if game['Name'] in self.allowed_games:
            if game['Price'] < self.allowed_games[game['Name']]:
                self.allowed_games[game['Name']] = game['Price']

    def parse(self, response):
        game_items = response.xpath('//div[@class="search listing-items"]//div[@class="item force-badge"]')

        for game_info in game_items:
            name = game_info.xpath('.//span[@class="title"]/text()').get()
            price = game_info.xpath('.//div[@class="price"]/text()').get()
            discount = game_info.xpath('.//div[@class="discount"]/text()').get()
            image = game_info.xpath('.//img/@data-src').get()
            link = game_info.xpath('.//a/@href').get()

            if name and price and name not in self.games:

                price = price.replace('€', '')

                game = {
                    'Name': name,
                    'Price': price,
                    'Link': link,
                    'Image': image,
                }

                if discount:
                    discount = discount.replace('-', '')
                    game['Discount'] = discount

                self.check_cheepest_price(game)
                if name in allowed_games and game not in self.game_list:
                    self.game_list.append(game)
                    self.games.append(name)
                    print(f"InstantGaming: {name} -----------------------")

        next_page = self.start_urls[0] + f"?type%5B0%5D=steam&page={self.page}"
        if self.page < 10: # 170
            self.page += 1
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = current_directory + '/data/ig.json'
        print(current_directory)
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(self.game_list, json_file, ensure_ascii=False, indent=4)