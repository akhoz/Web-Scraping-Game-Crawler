import scrapy


class G2aSpider(scrapy.Spider):
    name = "g2a"
    start_urls = ["https://www.g2a.com/es/category/games-c189?drm%5B0%5D=273&f%5Bdrm%5D%5B0%5D=8586&region%5B0%5D=878&region%5B1%5D=8355"]

    def parse(self, response):
        for game in response.xpath('//*[@id="c5a40d45-7a70-4e3b-9fa2-ac3dfbdefda3"]/section/div/div[2]/section/div[2]/div/ul'):
            print(game)



