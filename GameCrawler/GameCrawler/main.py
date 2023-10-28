import multiprocessing
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.instantGaming import InstantGamingSpider
from spiders.g2a import G2aSpider
#from spiders.eneba import EnebaSpider
from spiders.metacritic import MetacriticSpider
from spiders.howlongtobeat import HowlongtobeatSpider
from spiders.playStation import PlayStationSpider

spiders = [InstantGamingSpider ,G2aSpider, PlayStationSpider, MetacriticSpider, HowlongtobeatSpider]

#spiders = [InstantGamingSpider]
def run_spider(spider):
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider)
    process.start()

def main():
    jobs = []

    for spider in spiders:
        p = multiprocessing.Process(target=run_spider, args=(spider,))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

if __name__ == '__main__':
    main()