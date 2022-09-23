import os
import sys
import time 
import lxml 
import random 
sys.path.append(os.getcwd())

from downloader_test import Request_Downloader, \
    Html_Request_Downloader, Browser_Downloader, Downloader_Manager

def test_brave_downloader_on_MacOS():
    options = {
        "browser": "Brave", 
        "base_dir": "/home/administrator/news_crawler_development/src/crawler/crawler/lib/request_downloader", 
        "use_tor_proxy": False,
        "use_proxy": False,
        "headless": False,
        "fast_load": False, 
        "binary_location": "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser", 
        "driver_path": '/usr/local/bin/chromedriver'
    }

    firefox_downloader = Browser_Downloader(options)
    link = 'https://mbasic.facebook.com/groups/500613087057732'
    links = []
    for i in range(0, 100): 
        
        timeout = 30
        script = None
        result = firefox_downloader.get_html(link, script=script, timeout=timeout, options={"debug": False})
        html = lxml.etree.HTML(result)
        links.extend(html.xpath('//a/@href'))
        link = str(random.choice(links))
        if 'https' not in link:
            link = 'https://mbasic.facebook.com' + link 
        
        time.sleep(3)

    firefox_downloader.close()

if __name__ == "__main__":
    test_brave_downloader_on_MacOS()