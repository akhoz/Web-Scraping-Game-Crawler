import scrapy
import json
#from games import allowed_games
import os
#from GameCrawler.games import allowed_games



class PlayStationSpider(scrapy.Spider):
    name = "playStation"
    start_urls = ["https://store.playstation.com/en-us/category/877e5ce2-4afc-4694-9f69-4758e34e58cd/1"]
    pages = 2

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()

    def parse(self, response):
        games = response.xpath('//li[contains(@class, "psw-l-w-1/2@mobile-s psw-l-w-1/2@mobile-l psw-l-w-1/6@tablet-l psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop psw-l-w-1/8@max" )]')
        for game in games:
            game_name = game.xpath('.//span[contains(@class, "psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2")]/text()').extract_first()
            game_price = game.xpath('.//span[contains(@class, "psw-m-r-3")]/text()').extract_first()

            if game_name and game_price:
                game_price = game_price.replace("US$", "").strip()
                game_name = game_name.encode('utf-8').decode('ascii', 'ignore')

                with open('game_names.txt', 'a') as f:
                    f.write(f'"{game_name}",\n')

                self.data.append({
                    'name': game_name,
                    'price': game_price,
                })

        current_page = self.start_urls[0]
        index = current_page.rfind("/")
        current_page = current_page[:index+1]
        next_page = current_page + str(self.pages)
        if self.pages < 41:
            self.pages += 1
            yield response.follow(next_page, callback=self.parse)

'''
    def closed(self, reason):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = current_directory + '/data/ps.json'
        print(current_directory)
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
'''