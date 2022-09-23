from bot_xsmb.bots.tasks import (
    send_latest_xo_so_result_to_subcribers, 
    remind_subcribers_to_check_result
)
from bot_xsmb.crawler.tasks import crawl_xsmb_today_result
import pytest 
pytestmark = pytest.mark.django_db

class TestBotTask():
#     def test_alert_subcriber_latest_xsmb_result(self):
#         crawl_xsmb_today_result()
#         result = send_latest_xo_so_result_to_subcribers()
#         assert(result == True )

    def test_remind_subcriber_to_check_result(self): 
        result = remind_subcribers_to_check_result()
        assert(result == True )