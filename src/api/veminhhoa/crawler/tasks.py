from config import celery_app
from bot_xsmb.crawler.crawler import (
    XSMB_Crawler, 
    XSMB_Crawler_KetQua_VN 
)

from bot_xsmb.kq_xo_so.models import (
    check_if_specific_xsmb_result_exist
)
import django
import datetime  
import time 

@celery_app.task()
def crawl_xsmb_today_result(): 
    crawler = XSMB_Crawler()
    strategy = XSMB_Crawler_KetQua_VN()
    crawler.register_strategy(strategy)
    
    retry = 3 
    count = 0 
    while count < retry: 
        xsmb_model, has_updated = crawler.crawl_today_data()
        if xsmb_model and has_updated:
            xsmb_model.save()
            break 
        else:
            count += 1 
            time.sleep(5)
        
    return True 

@celery_app.task()
def crawl_xsmb_latest_results(number=20, sleep_between_crawl=10): 
    crawler = XSMB_Crawler()
    strategy = XSMB_Crawler_KetQua_VN()
    crawler.register_strategy(strategy)

    count = 0 
    now_date = django.utils.timezone.now().date()
    current_date = now_date 
    while count < number:
        temp_date = current_date - datetime.timedelta(days=1)
        if not check_if_specific_xsmb_result_exist(temp_date):
            xsmb_model = crawler.crawl_specific_date_data(temp_date, use_proxy=True)
            if xsmb_model:
                if xsmb_model.ngay_trao_giai == temp_date:
                    xsmb_model.save()
                    count += 1 
            time.sleep(sleep_between_crawl)

        current_date = temp_date 
    return True 
