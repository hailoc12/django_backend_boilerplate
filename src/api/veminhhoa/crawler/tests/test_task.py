from bot_xsmb.crawler.tasks import (
    crawl_xsmb_today_result, 
    crawl_xsmb_latest_results
)
import pytest 

pytestmark = pytest.mark.django_db

# class TestCrawlTasks():
#     def test_crawl_xsmb_today_result_task(self):
#         result = crawl_xsmb_today_result()
#         assert(result == True)

#     def test_crawl_xsmb_latest_results(self):
#         result = crawl_xsmb_latest_results(number=5, sleep_between_crawl=3)
#         assert(result == True)
            