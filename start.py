
import sys
from tasks.basic_task import BasicTask
from tasks.douban_film_data import DoubanMovieTask

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from spinelle.spiders.douban_movie import DoubanMovieSpider

# See https://github.com/sebdah/scrapy-mongodb/commit/4723d7af5c2a6867e51e84d75061e0b2ac148084
SETTINGS = get_project_settings()


def register_douban_moive_crawl():
    crawler_process = CrawlerProcess(settings=SETTINGS)
    crawler_process.crawl(DoubanMovieSpider)
    crawler_process.start()

register_crawl_mission = dict()
register_crawl_mission['douban-movie'] = DoubanMovieTask

register_crawl_mission['crawl-douban-movie'] = register_douban_moive_crawl

if __name__ == "__main__":
    if sys.argv and len(sys.argv) <= 1:
        sys.exit(0)

    command = sys.argv[1]
    mission_class = register_crawl_mission.get(command, None)
    if callable(mission_class):
        mission_instance = mission_class()
        # Handle BasicTask Mission.
        if isinstance(mission_instance, BasicTask):
            mission_instance.start_task()
