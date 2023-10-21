import scrapy
import json
from GameCrawler.games import allowed_games

class HowlongtobeatSpider(scrapy.Spider):
    name = "howlongtobeat"
    start_urls = ["https://howlongtobeat.com/?q=recently%2520updated"]

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()

    def parse(self, response):
        game_items = response.xpath('//li[contains(@class, "back_darkish GameCard_search_list__IuMbi")]')
        print(type(game_items))
        print(len(game_items))

        for game in game_items:
            game_name = game.xpath('.//h3/a/@title').get()
            completionist_time = game.xpath('.//div[contains(text(), "Completionist")]/following-sibling::div[contains(@class, "time")]/text()').get()
            
            if game_name and completionist_time:
                if game_name not in self.scraped_game_names:
                    item =  {
                        'Game Name': game_name.strip(),
                        'Completionist Hours': completionist_time.strip()
                    }

                    if game_name in allowed_games:
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
                        print(f"{game_name} added")

    def closed(self, reason):
        with open('GameCrawler/outputs/hltb_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)