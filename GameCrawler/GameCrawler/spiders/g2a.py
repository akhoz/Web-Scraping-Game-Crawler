import scrapy
import json
from GameCrawler.games import allowed_games

class G2aSpider(scrapy.Spider):
    name = "g2a"
    start_urls = ["https://www.g2a.com/es/category/gaming-c1"]
    pages = 2

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()

    def parse(self, response):
        games = response.xpath('//li[contains(@class, "indexes__StyledProductBox-wklrsw-91")]')

        for game in games:
            game_name = game.xpath('@name').extract_first()
            game_name = game_name.split(' (')[0].strip()
            game_price = ''.join(game.xpath('.//span[contains(@data-locator, "zth-price")]/text()').extract()).strip()
            game_discount = ''.join(game.xpath('.//span[contains(@data-locator, "zth-badge")]/text()').extract()).strip()
            game_discount = game_discount.replace('-', '')

            if game_name and game_price:
                if game_name not in self.scraped_game_names:
                    item = {
                        "Name": game_name,
                        "Price": game_price,
                    }

                    if game_discount:
                        item["Discount"] = game_discount
                    if game_name in allowed_games:
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
                        print(f"{game_name} added")
        
        next_page = self.start_urls[0] + f"?page={self.pages}"
        if self.pages < 999:
            self.pages += 1
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        with open('GameCrawler/outputs/g2a_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)