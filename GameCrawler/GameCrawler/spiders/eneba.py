import scrapy
import json
from GameCrawler.games import allowed_games
from urllib.parse import urljoin

class EnebaSpider(scrapy.Spider):
    name = 'eneba'
    start_urls = ['https://www.eneba.com/latam/store/games']

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()

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
                if game_name not in self.scraped_game_names:
                    item = {
                        "Name": game_name,
                        "Price": game_price,
                    } 

                    if game_name in allowed_games:
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
                        print(f"{game_name} added")

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page:
            next_page_url = urljoin(response.url, next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def closed(self, reason):
        with open('GameCrawler/outputs/eneba_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
