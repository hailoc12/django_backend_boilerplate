from bot_xsmb.crawler.lib.request_downloader.downloader import Request_Downloader 
from bot_xsmb.crawler.lib.utils import print_exception
from bot_xsmb.kq_xo_so.models import XoSoMienBac
import pandas as pd
import lxml
import datetime
import time 
import json
from typing import Tuple


class CrawlStrategy():
    pass

class XSMB_Crawl_Strategy(CrawlStrategy):
    def __init__(self):
        self.crawl_current_date_url = 'https://ketqua.vn'
        self.crawl_specific_date_url = 'https://ketqua.vn/xsmb/{0}'
    
    def get_page_html(self, url:str, use_proxy=False): 
        downloader = Request_Downloader(use_proxy=use_proxy)
        html = downloader.get_html(url)
        return str(html)

    def crawl_today_data(self): 
        pass 

    def crawl_specific_date_data(self, date:datetime.date):
        pass 


class XSMB_Crawler_KetQua_VN(XSMB_Crawl_Strategy): 
    def _parse_result_from_html(self, html):
        if html: 
            tree = lxml.etree.HTML(html)
            try: 
                date_str = tree.xpath('//div[@id="kqxs-box"]/table//th//*[contains(text(), "ngày")]/text()')[0].strip()
                kq_date = datetime.datetime.strptime(date_str[-10:], '%d/%m/%Y').date()
                kqsx = json.loads(tree.xpath('//div[@class="data-kqxs hidden"]/text()')[0])
                has_today_update = kq_date == datetime.date.today()

                xsmb_result = XoSoMienBac(
                    ngay_trao_giai = kq_date, 
                    giai_dac_biet = kqsx['g0'].split('-'),
                    giai_nhat = kqsx['g1'].split('-'),
                    giai_nhi = kqsx['g2'].split('-'),
                    giai_ba = kqsx['g3'].split('-'),
                    giai_tu = kqsx['g4'].split('-'),
                    giai_nam = kqsx['g5'].split('-'),
                    giai_sau = kqsx['g6'].split('-'),
                    giai_bay = kqsx['g7'].split('-')
                )
                xsmb_result.auto_calculate_loto()
                return xsmb_result, has_today_update
            except Exception as e:
                print(e)
                return None, False 
        return None, False 

    def crawl_today_data(self)-> XoSoMienBac: 
        has_today_update = False 
        html = self.get_page_html(url=self.crawl_current_date_url)
        xsmb_result, has_today_update = self._parse_result_from_html(html)
        return xsmb_result, has_today_update
    
    def crawl_specific_date_data(self, date:datetime.date, use_proxy=False) -> XoSoMienBac:
        url = self.crawl_specific_date_url.format(date.strftime('%d-%m-%Y'))
        html = self.get_page_html(url=url, use_proxy=use_proxy)
        xsmb_result, has_today_update = self._parse_result_from_html(html)
        return xsmb_result



class Crawler():
    pass 

class XSMB_Crawler(Crawler):
    crawl_strategies = []
    def register_strategy(self, xsmb_crawl_strategy:XSMB_Crawl_Strategy):
        self.crawl_strategies.append(xsmb_crawl_strategy)

    def unregister_strategy(self, xsmb_crawl_strategy:XSMB_Crawl_Strategy):
        self.crawl_strategies.remove(xsmb_crawl_strategy)

    def crawl_today_data(self)->Tuple[XoSoMienBac, bool]:
        for strategy in self.crawl_strategies: 
            xsmb_model, has_today_updated = strategy.crawl_today_data()
            if xsmb_model:
                return xsmb_model, has_today_updated
                break 
        return None, False 

    def crawl_specific_date_data(self, date:datetime.date, use_proxy=True)->XoSoMienBac:
        for strategy in self.crawl_strategies: 
            xsmb_model = strategy.crawl_specific_date_data(date, use_proxy=use_proxy)
            if xsmb_model:
                return xsmb_model
                break 
        return None

def crawl_xsmb_specific_date_data(crawl_date:datetime.date, retry=3)->XoSoMienBac: 
    crawler = XSMB_Crawler()
    count = 0 
    while count < retry: 
        result = crawler.crawl_specific_date_data(crawl_date)
        if result:
            return result 
        else:
            count += 1 
            time.sleep(5)
    return None 


def change_sxmb(df):
    # Chuyển table web về dataframe dạng yêu cầu
    df1 = pd.DataFrame({
        'Thứ':[' '.join([df.columns[0].split()[0], df.columns[0].split()[1]])],
        'Ngày':[df.columns[0].split()[3]],
        'Giải đặc biệt':[df.iloc[1][1]],
        'Giải nhất':[df.iloc[2][1]],
        'Giải nhì':[','.join([df.iloc[3][1][(i*5):((i+1)*5)] for i in range(2)])],
        'Giải ba':[','.join([df.iloc[4][1][(i*5):((i+1)*5)] for i in range(6)])],
        'Giải tư':[','.join([df.iloc[5][1][(i*4):((i+1)*4)] for i in range(4)])],
        'Giải năm':[','.join([df.iloc[6][1][(i*4):((i+1)*4)] for i in range(6)])],
        'Giải sáu':[','.join([df.iloc[7][1][(i*3):((i+1)*3)] for i in range(3)])],
        'Giải bảy':[','.join([df.iloc[8][1][(i*2):((i+1)*2)] for i in range(4)])]
    })    
    return df1

def get_data_50():
    # Lấy dữ liệu trong 50 ngày gần nhất
    url = 'http://ketqua1.net/so-ket-qua-truyen-thong/60'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    contents = tree.xpath('//*[@id="result_tab_mb"]')
    df_all = []
    for i in range(len(contents)):
        df = pd.read_html(etree.tostring(contents[i],method='html'))[0]
        df_all.append(change_sxmb(df)) 
    df_50 = pd.concat(df_all).reset_index(drop=True).iloc[0:50] 
    return df_50
