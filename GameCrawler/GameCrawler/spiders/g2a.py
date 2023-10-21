import scrapy
import json
from GameCrawler.games import allowed_games

class G2aSpider(scrapy.Spider):
    name = "g2a"
    start_urls = ["https://www.g2a.com/es/category/gaming-c1"]

    def __init__(self):
        self.data = []

    def parse(self, response):
        games = response.xpath('//li[contains(@class, "indexes__StyledProductBox-wklrsw-91")]')

        for game in games:
            game_name = game.xpath('@name').extract_first()
            game_name = game_name.split(' (')[0].strip()
            game_price = ''.join(game.xpath('.//span[contains(@data-locator, "zth-price")]/text()').extract()).strip()
            game_discount = ''.join(game.xpath('.//span[contains(@data-locator, "zth-badge")]/text()').extract()).strip()
            game_discount = game_discount.replace('-', '')  

            if game_name and game_price:
                item = {
                    "Name": game_name,
                    "Price": game_price,
                }

                if game_discount:
                    item["Discount"] = game_discount

                game_already_added = False
                if game_name in allowed_games:
                    for existing_item in self.data:
                        if existing_item["Name"] == game_name:
                            if float(game_price) < float(existing_item["Price"]):
                                existing_item["Price"] = game_price
                                if game_discount:
                                    existing_item["Discount"] = game_discount
                                game_already_added = True
                                print(f"{game_name} updated")
                    
                    if not game_already_added:
                        self.data.append(item)
                        print(f"{game_name} added")
        print(self.data)

    def closed(self, reason):
        with open('GameCrawler/outputs/g2a_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
