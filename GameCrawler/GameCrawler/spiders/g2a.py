import scrapy
import json
from games import allowed_games
import os

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
            game_price = ''.join(game.xpath('.//span[contains(@data-locator, "zth-price")]/text()').extract()).strip()
            game_discount = ''.join(game.xpath('.//span[contains(@data-locator, "zth-badge")]/text()').extract()).strip()
            product_link = game.xpath('.//h3/a/@href').extract_first()
            #game_image = game.xpath('.//a/img/@src').extract_first()


            if game_name and game_price:
                if game_name not in self.scraped_game_names:
                    game_name = game_name.split(' (')[0].strip()
                    game_discount = game_discount.replace('-', '')
                    product_link = 'https://www.g2a.com' + product_link
                    item = {
                        "name": game_name,
                        "price": game_price,
                        "link": response.urljoin(product_link),
                        #"image": game_image
                    }

                    if game_discount:
                        item["discount"] = game_discount
                    if game_name in allowed_games:
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
                        print(f"G2a: {game_name} -----------------------")    
        next_page = self.start_urls[0] + f"?page={self.pages}"
        if self.pages < 279: # 279
            self.pages += 1
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = current_directory + '/data/g2a.json'
        print(current_directory)
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
