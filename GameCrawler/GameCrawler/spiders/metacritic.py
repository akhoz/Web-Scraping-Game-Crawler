import scrapy
import json
from games import allowed_games
import os

class MetacriticSpider(scrapy.Spider):
    name = "metacritic"
    start_urls = ["https://www.metacritic.com/browse/game/"]
    pages = 2

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()

    def parse(self, response):
        games = response.xpath('//div[contains(@class, "c-finderProductCard c-finderProductCard-game")]')
        for game in games:
            game_name = game.xpath('.//div[@data-title]/@data-title').extract_first()
            metascore = game.xpath('.//div[contains(@class, "c-siteReviewScore_background")]/div/span/text()').extract_first()

            if game_name:
                if game_name not in self.scraped_game_names:
                    if game_name in allowed_games:
                        if not metascore:
                            metascore = "--"
                        item = {
                            "Name": game_name,
                            "Metascore": metascore
                        }
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
                        print(f"Metacritic: {game_name} -----------------------")
                        
        next_page = self.start_urls[0] + f"?releaseYearMin=1910&releaseYearMax=2023&page={self.pages}"
        if self.pages < 543: # 543
            self.pages += 1
            yield response.follow(next_page, callback=self.parse)
        
    def closed(self, reason):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = current_directory + '/data/metacritic.json'
        print(current_directory)
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)