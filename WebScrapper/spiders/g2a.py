import scrapy
import json
from allowed import allowed_games

class G2aSpider(scrapy.Spider):
    name = "g2a"
    start_urls = ["https://www.g2a.com/es/category/gaming-c1"]
    pages = 2

    def __init__(self):
        self.game_list = []
        self.allowed_games = set()
        self.file_path = "./Data/games.json" # esto!

    def parse(self, response):
        games = response.xpath('//li[contains(@class, "indexes__StyledProductBox-wklrsw-91")]')

        for game in games:
            game_name = game.xpath('@name').extract_first()
            game_name = game_name.split(' (')[0].strip()
            game_price = ''.join(game.xpath('.//span[contains(@data-locator, "zth-price")]/text()').extract()).strip()
            game_discount = ''.join(game.xpath('.//span[contains(@data-locator, "zth-badge")]/text()').extract()).strip()
            game_discount = game_discount.replace('-', '')

            if game_name and game_price and game_discount:
                if game_name not in self.game_list and game_name in allowed_games:
                    item = {
                        "Name": game_name,
                        "Price": game_price,
                        "Discount": game_discount
                    }
                    self.game_list.append(item)
        
        next_page = self.start_urls[0] + f"?page={self.pages}"
        if self.pages < 500:
            self.pages += 1
            yield response.follow(next_page, callback=self.parse)
        try:
            with open(self.file_path, 'r') as f:
                data_file = json.load(f)
                data_file.extend(self.game_list)
            with open(self.file_path, 'w') as f:
                json.dump(data_file, f, indent=4)
                # json.dump(self.game_list, f, indent=4)
        except FileNotFoundError:
            with open(self.file_path, 'w') as f:
                json.dump(self.game_list, f, indent=4)

