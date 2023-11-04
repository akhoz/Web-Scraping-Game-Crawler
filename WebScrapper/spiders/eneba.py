import scrapy
import json
from allowed import allowed_games
from urllib.parse import urljoin

class EnebaSpider(scrapy.Spider):
    name = 'eneba'
    start_urls = ['https://www.eneba.com/latam/store/games']

    def __init__(self):
        self.game_list = []
        self.allowed_games = set()
        self.file_path = "./Data/games.json" # esto!

    def parse(self, response):
        games = response.xpath('//div[contains(@class, "pFaGHa WpvaUk")]')
        for game in games:
            game_name = game.xpath('.//span[contains(@class, "YLosEL")]//text()').get()
            game_name = game_name.split(' (')[0].strip()
            game_name = game_name.split(' Steam')[0].strip()
            game_price = game.xpath('.//span[contains(@class, "L5ErLT")]//text()').get()
            game_price = game_price.split(' €')[0].strip()
            game_price = game_price.replace('€', '').strip()
    
            if game_name and game_price:
                if game_name not in self.game_list:
                    item = {
                        "Name": game_name,
                        "Price": game_price,
                    } 
                    if game_name in allowed_games:
                        self.game_list.append(item)

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page:
            next_page_url = urljoin(response.url, next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        try:
            with open(self.file_path, 'r') as f:
                data_file = json.load(f)
                data_file.extend(self.game_list)

        except FileNotFoundError:
            data_file = self.game_list

        with open(self.file_path, 'w') as f:
            json.dump(data_file, f, indent=4)
