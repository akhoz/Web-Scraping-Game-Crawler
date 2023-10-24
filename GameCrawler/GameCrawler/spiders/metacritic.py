import scrapy


class MetacriticSpider(scrapy.Spider):
    name = "metacritic"
    start_urls = ["https://www.metacritic.com/browse/game/"]

    def parse(self, response):
        games = response.xpath('//div[contains(@class, "c-finderProductCard c-finderProductCard-game")]')
        for game in games:
            game_name = game.xpath('.//div[@data-title]/@data-title').extract_first()
            metascore = game.xpath('.//div[contains(@class, "c-siteReviewScore")]/span/text()').extract_first()
            print(f"Game Name: {game_name}")
            print(f"Metascore: {metascore}")