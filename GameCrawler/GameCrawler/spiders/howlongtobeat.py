import scrapy
import time
import json
from games import allowed_games
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# firefox_path = "/usr/bin/geckodriver"
# driver = webdriver.Firefox(executable_path=firefox_path)

class HowlongtobeatSpider(scrapy.Spider):
    name = "howlongtobeat"
    start_urls = ["https://howlongtobeat.com/?q="]

    custom_settings = {
        'USER_AGENT':  'non_standar_user (https://howlongtobeat.com/?q=recently%2520updated)'
    }

    def __init__(self):
        self.data = []
        self.scraped_game_names = set()

    def parse(self, response):
        game_items = response.xpath('//li[contains(@class, "back_darkish GameCard_search_list__IuMbi")]')
        print(type(game_items))
        print(len(game_items))

        for game in game_items:
            game_name = game.xpath('.//h3/a/@title').get()
            completionist_time = game.xpath('.//div[contains(text(), "Completionist")]/following-sibling::div[contains(@class, "time")]/text()').get()

            if game_name and completionist_time:
                if game_name not in self.scraped_game_names:
                    completionist_time = completionist_time.replace("½", ".5")
                    item = {
                        'name': game_name.strip(),
                        'tta': completionist_time.strip()
                    }

                    if game_name in allowed_games:
                        self.data.append(item)
                        self.scraped_game_names.add(game_name)
                        print(f"HowLongToBeat: {game_name} -----------------------")

        driver = webdriver.Firefox()
        driver.get(response.url)

        for game_name in allowed_games:

            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"MainNavigation_search_box__UUnYc")))

            response = scrapy.Selector(text=driver.page_source)
            game_items = response.xpath('//li[contains(@class, "back_darkish GameCard_search_list__IuMbi")]')

            search_box.clear()
            search_box.send_keys(game_name)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)

            for game in game_items:
                game_name = game.xpath('.//h3/a/@title').get()
                completionist_time = game.xpath('.//div[contains(text(), "Completionist")]/following-sibling::div[contains(@class, "time")]/text()').get()

                if game_name and completionist_time:
                    if game_name not in self.scraped_game_names:
                        completionist_time = completionist_time.replace("½", ".5")
                        item = {
                            'name': game_name.strip(),
                            'tta': completionist_time.strip()
                        }

                        if game_name in allowed_games:
                            self.data.append(item)
                            self.scraped_game_names.add(game_name)
                            print(f"HowLongToBeat: {game_name} -----------------------")

        driver.quit()

    def closed(self, reason):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        path = current_directory + '/data/hltb.json'
        print(current_directory)
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)
