from bot_xsmb.kq_xo_so.models import XoSoMienBac
from bot_xsmb.crawler.crawler import crawl_xsmb_specific_date_data
import datetime 

def get_xsmb_specific_date_result(crawl_date:datetime.datetime.date, add_to_database=True, retry=1)-> XoSoMienBac: 
    result = XoSoMienBac.objects.filter(
        ngay_trao_giai = crawl_date
    ).first()
    
    if result:
        return result

    result = crawl_xsmb_specific_date_data(crawl_date, retry=retry)
    if result and add_to_database:
        result.save()
    return result 
    

        
