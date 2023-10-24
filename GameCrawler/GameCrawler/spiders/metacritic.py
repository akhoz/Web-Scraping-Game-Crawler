import scrapy
import json
from GameCrawler.games import allowed_games


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
            metascore = game.xpath('.//div[contains(@class, "c-siteReviewScore")]/span/text()').extract_first()

            if game_name and metascore:
                if game_name not in self.scraped_game_names:
                    if game_name in allowed_games:
                        item = {
                            "Name": game_name,
                            "Metascore": metascore
                        }
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
        next_page = self.start_urls[0] + f"?releaseYearMin=1910&releaseYearMax=2023&page={self.pages}"
        if self.pages < 542:
            self.pages += 1
            yield response.follow(next_page, callback=self.parse)
        
    def closed(self, reason):
        with open('GameCrawler/outputs/metacritic_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)