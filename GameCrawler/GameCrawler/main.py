import multiprocessing
import json
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.instantGaming import InstantGamingSpider
from spiders.g2a import G2aSpider
#from spiders.eneba import EnebaSpider
from spiders.metacritic import MetacriticSpider
from spiders.howlongtobeat import HowlongtobeatSpider
from spiders.playStation import PlayStationSpider

spiders = [MetacriticSpider, G2aSpider, PlayStationSpider, InstantGamingSpider, HowlongtobeatSpider]

#spiders = [InstantGamingSpider]
def run_spider(spider):
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider)
    process.start()

def merge_data():
    current_directory = os.path.dirname(os.path.realpath(__file__))

    with open(f'{current_directory}/spiders/data/g2a.json', 'r') as file:
        g2a = json.load(file)

    with open(f'{current_directory}/spiders/data/ig.json', 'r') as file:
        ig = json.load(file)

    with open(f'{current_directory}/spiders/data/ps.json', 'r') as file:
        ps = json.load(file)

    with open(f'{current_directory}/spiders/data/metacritic.json', 'r') as file:
        mc = json.load(file)

    merged_data = g2a + ig + ps

    data_dict = {}

    for game in merged_data:
        game_name = game['Name']
        game_price = float(game['Price'])

        if game_name in data_dict:
            if game_price < float(data_dict[game_name]['Price']):
                data_dict[game_name] = game
        else:
            data_dict[game_name] = game

    for game_name, game_info in data_dict.items():
        if game_name in mc:
            game_info['Metascore'] = mc[game_name]['Metascore']
        elif 'Metascore' not in game_info:
            game_info['Metascore'] = "--"

    data_list = list(data_dict.values())

    with open('data.json', 'w') as file:
        json.dump(data_list, file, indent=4)

def main():
    jobs = []

    for spider in spiders:
        p = multiprocessing.Process(target=run_spider, args=(spider,))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

    merge_data()

if __name__ == '__main__':
    main()