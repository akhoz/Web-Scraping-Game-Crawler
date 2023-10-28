import scrapy
import json
from GameCrawler.games import allowed_games
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HowlongtobeatSpider(scrapy.Spider):
    name = "howlongtobeat"
    start_urls = ["https://howlongtobeat.com/?q=recently%2520updated"]

    custom_settings = {
        'USER_AGENT':  'non_standar_user (https://howlongtobeat.com/?q=recently%2520updated)'
    }

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()

    def navigate_to_next_page(self, driver):
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'Pagination_right__GwBE_')]"))
            )
            next_button.click()
            return True
        except Exception as e:
            print(f"Failed to navigate to the next page: {e}")
            return False

    def parse(self, response):
        game_items = response.xpath('//li[contains(@class, "back_darkish GameCard_search_list__IuMbi")]')
        print(type(game_items))
        print(len(game_items))

        for game in game_items:
            game_name = game.xpath('.//h3/a/@title').get()
            completionist_time = game.xpath('.//div[contains(text(), "Completionist")]/following-sibling::div[contains(@class, "time")]/text()').get()

            if game_name and completionist_time:
                if game_name not in self.scraped_game_names:
                    item = {
                        'Game Name': game_name.strip(),
                        'Completionist Hours': completionist_time.strip()
                    }

                    if game_name in allowed_games:
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
                        print(f"HowLongToBeat: {game_name} -----------------------")

        driver = webdriver.Edge()
        driver.get(response.url)

        while self.navigate_to_next_page(driver):
            response = scrapy.Selector(text=driver.page_source)
            game_items = response.xpath('//li[contains(@class, "back_darkish GameCard_search_list__IuMbi")]')

            for game in game_items:
                game_name = game.xpath('.//h3/a/@title').get()
                completionist_time = game.xpath('.//div[contains(text(), "Completionist")]/following-sibling::div[contains(@class, "time")]/text()').get()

                if game_name and completionist_time:
                    if game_name not in self.scraped_game_names:
                        item = {
                            'Game Name': game_name.strip(),
                            'Completionist Hours': completionist_time.strip()
                        }

                        if game_name in allowed_games:
                            self.data.append(item)
                            self.scraped_game_names.add(game_name)
                            print(f"HowLongToBeat: {game_name} -----------------------")

        driver.quit()
