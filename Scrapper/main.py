import multiprocessing
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.instantGaming import IG
from spiders.g2a import G2aSpider
from spiders.eneba import EnebaSpider

# spiders = [IG, G2aSpider, EnebaSpider]
spiders = [IG]

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
