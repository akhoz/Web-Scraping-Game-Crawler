import multiprocessing
import json
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.instantGaming import InstantGamingSpider
from spiders.g2a import G2aSpider
from spiders.metacritic import MetacriticSpider
from spiders.howlongtobeat import HowlongtobeatSpider
from spiders.playStation import PlayStationSpider

# spiders = [MetacriticSpider, G2aSpider, PlayStationSpider, InstantGamingSpider, HowlongtobeatSpider]
spiders = [HowlongtobeatSpider]

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

    with open(f'{current_directory}/spiders/data/hltb.json', 'r') as file:
        hltb = json.load(file)

    merged_data = g2a + ig + ps

    data_dict = {}

    for game in merged_data:
        game_name = game['name']
        game_price = float(game['price'])

        if game_name in data_dict:
            if game_price < float(data_dict[game_name]['price']):
                data_dict[game_name] = game
        else:
            data_dict[game_name] = game

    for game in mc:
        if game['name'] in data_dict:
            data_dict[game['name']]['metascore'] = game['metascore']

    for game in hltb:
        if game['name'] in data_dict:
            data_dict[game['name']]['tta'] = game['tta']

    for game in data_dict.values():
        if "metascore" not in game:
            game["metascore"] = "--"
        if "tta" not in game:
            game["tta"] = "--"
            
    data_list = list(data_dict.values())

    with open('data.json', 'w') as file:
        json.dump(data_list, file, indent=4)

def asing_id():
    with open('data.json', 'r') as file:
        data = json.load(file)

    for index, game in enumerate(data, start=1):
        game['id'] = index

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # jobs = []

    # for spider in spiders:
    #     p = multiprocessing.Process(target=run_spider, args=(spider,))
    #     jobs.append(p)
    #     p.start()

    # for job in jobs:
    #     job.join()

    merge_data()
    asing_id()

if __name__ == '__main__':
    main()
