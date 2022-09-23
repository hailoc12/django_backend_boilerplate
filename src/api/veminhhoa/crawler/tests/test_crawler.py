from bot_xsmb.crawler.crawler import (
    XSMB_Crawler, 
    XSMB_Crawler_KetQua_VN 
)

import datetime 
import django

class Test_XSMB_Crawler():
    # def test_get_today_page_html(self): 
    #     crawler = XSMB_Crawler_KetQua_VN()
    #     html = crawler.get_page_html(crawler.crawl_current_date_url)
    #     assert (html is not None)

    def test_get_today_result(self): 
        crawler = XSMB_Crawler()
        strategy = XSMB_Crawler_KetQua_VN()
        crawler.register_strategy(strategy)
        result, has_updated = crawler.crawl_today_data()
        assert (result is not None)

    # def test_get_specific_date_result(self): 
    #     crawler = XSMB_Crawler()
    #     strategy = XSMB_Crawler_KetQua_VN()
    #     crawler.register_strategy(strategy)
    #     date = datetime.date(2021, 1, 1)
    #     result = crawler.crawl_specific_date_data(date)
    #     assert (result is not None)

    # def test_get_specific_date_result_with_proxy(self): 
    #     crawler = XSMB_Crawler()
    #     strategy = XSMB_Crawler_KetQua_VN()
    #     crawler.register_strategy(strategy)
    #     date = datetime.date(2021, 1, 1)
    #     result = crawler.crawl_specific_date_data(date, use_proxy=True)
    #     assert (result is not None)


