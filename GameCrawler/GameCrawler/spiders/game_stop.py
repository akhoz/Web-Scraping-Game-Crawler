import scrapy


class GameStopSpider(scrapy.Spider):
    name = 'gamestop'
    start_urls = ['https://www.gamestop.com/video-games/playstation-5']

    def parse(self, response):
        
        print(response.xpath('//*[@id="394826"]/div[1]/div[1]/div/text()'))
        for product in response.xpath('//*[@id="394826"]/div[1]/div[1]/div'):
            yield {
                'name': product.css('.render-tile-name::text').get()
            }
