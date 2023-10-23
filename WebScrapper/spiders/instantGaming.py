import scrapy
import json
# from Scrapper.allowed import allowed_games
from allowed import allowed_games
import os


class IG(scrapy.Spider):
    name = "IG" # Name of the Spider
    start_urls = ["https://www.instant-gaming.com/en/search/"] # Starting url
    page = 1 # IDX of the page

    def __init__(self):
        self.games = []
        self.game_list = []
        self.allowed_games = set()
        self.file_path = "./Data/games.json" # esto!

    def check_cheepest_price(self, game):
        if game['name'] in self.allowed_games:
            if game['price'] < self.allowed_games[game['name']]:
                self.allowed_games[game['name']] = game['price']

    def parse(self, response):
        game_items = response.xpath('//div[@class="search listing-items"]//div[@class="item force-badge"]')

        for game_info in game_items:
            name = game_info.xpath('.//span[@class="title"]/text()').get()
            price = game_info.xpath('.//div[@class="price"]/text()').get()
            discount = game_info.xpath('.//div[@class="discount"]/text()').get()

            if name and price and discount and name not in self.games:
                game = {
                    'name': name,
                    'price': price,
                    'discount': discount
                }
                if name in allowed_games and game not in self.game_list:
                    self.game_list.append(game)
                    self.games.append(name)
                    print(self.games)

        next_page = self.start_urls[0] + f"?type%5B0%5D=steam&page={self.page}"
        if self.page < 140:
            self.page += 1
            yield response.follow(next_page, callback=self.parse)

    def close(self, reason):     
        try:
            with open(self.file_path, 'r') as f:
                data_file = json.load(f)
                data_file.extend(self.game_list)
        except FileNotFoundError:
            data_file = self.game_list

        with open(self.file_path, 'w') as f:
            json.dump(data_file, f, indent=4)

