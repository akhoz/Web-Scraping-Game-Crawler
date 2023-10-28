import scrapy
import json
import os
import requests
from games import allowed_games
from urllib.parse import urljoin

class PlayStationSpider(scrapy.Spider):
    name = "playStation"
    start_urls = ["https://store.playstation.com/en-us/category/85448d87-aa7b-4318-9997-7d25f4d275a4/1"]

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()
        self.pages = 1

    def parse(self, response):
        games = response.xpath('//li[contains(@class, "psw-l-w-1/2@mobile-s psw-l-w-1/2@mobile-l psw-l-w-1/6@tablet-l psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop psw-l-w-1/8@max")]')
        
        for game in games:
            game_name = game.xpath('.//span[contains(@class, "psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2")]/text()').extract_first()
            game_price = game.xpath('.//span[contains(@class, "psw-m-r-3")]/text()').extract_first()
            game_discount = game.xpath('.//span[contains(@class, "psw-body-2 psw-badge__text psw-badge--none psw-text-bold psw-p-y-0 psw-p-2 psw-r-1 psw-l-anchor")]/text()').extract_first()
            game_link = game.xpath('.//a/@href').extract_first()
            game_image = game.xpath('.//img/@src').extract_first()

            if game_name in allowed_games and game_price:
                game_price = game_price.replace("US$", "")
                
                if game_price == "Free" or game_price == "Included":
                    game_price = "0"

                else:
                    game_price = game_price[1:]

                game_name = game_name.encode('utf-8').decode('ascii', 'ignore')

                base_url = "https://store.playstation.com"
                game_link = urljoin(base_url, game_link)
                game_image = urljoin(base_url, game_image)
                item = {
                    "Name": game_name,
                    "Price": game_price,
                    "Link": game_link,
                    "Image": game_image
                }

                if game_discount:
                    game_discount = game_discount.replace("-", "")
                    item["Discount"] = game_discount

                self.data.append(item)
                print(f"PlayStation: {game_name} -----------------------")

        if self.pages < 10: # 279
            next_page = f"https://store.playstation.com/en-us/category/877e5ce2-4afc-4694-9f69-4758e34e58cd/{self.pages+1}"
            yield response.follow(next_page, callback=self.parse)
            self.pages += 1

    def closed(self, reason):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = current_directory + '/data/ps.json'
        print(current_directory)
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
