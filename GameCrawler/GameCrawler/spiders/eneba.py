import scrapy


class EnebaSpider(scrapy.Spider):
    name = 'eneba'
    start_urls = ['https://www.eneba.com/latam/store/games']



    def parse(self, response):
        games = response.xpath('//div[contains(@class, "pFaGHa WpvaUk")]')
        for game in games:
            game_name = game.xpath('.//span[contains(@class, "YLosEL")]//text()').get()
            game_name = game_name.split(' (')[0].strip()
            game_name = game_name.split(' Steam')[0].strip()
            game_price = game.xpath('.//span[contains(@class, "L5ErLT")]//text()').get()
            game_price = game_price.split(' €')[0].strip()
            game_price = game_price.replace('€', '').strip()
    
            print(game_name, game_price)    

