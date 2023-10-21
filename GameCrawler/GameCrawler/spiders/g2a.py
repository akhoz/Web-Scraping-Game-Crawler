import scrapy
import json

class G2aSpider(scrapy.Spider):
    name = "g2a"
    start_urls = ["https://www.g2a.com/es/category/games-c189?drm%5B0%5D=273&f%5Bdrm%5D%5B0%5D=8586&region%5B0%5D=878&region%5B1%5D=8355"]
    
    def __init__(self):
        self.data = []

    def parse(self, response):
        games = response.xpath('//li[contains(@class, "indexes__StyledProductBox-wklrsw-91")]')
        
        for game in games:
            game_name = game.xpath('@name').extract_first()
            game_price = ''.join(game.xpath('.//span[contains(@data-locator, "zth-price")]/text()').extract()).strip()
            game_discount = ''.join(game.xpath('.//span[contains(@data-locator, "zth-badge")]/text()').extract()).strip()
            game_discount = game_discount.replace('-', '')  # Eliminar el signo "-"
            
            if game_name and game_price:
                item = {
                    "Name": game_name,
                    "Price": game_price,
                }
                
                if game_discount:
                    item["Discount"] = game_discount
                
                self.data.append(item)
                print(item)
                
        next_page_url = response.xpath('//a[contains(@class, "nextButton")]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

    def closed(self, reason):
        # Guardar los datos recopilados en un archivo JSON
        with open('GameCrawler/outputs/g2a_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
