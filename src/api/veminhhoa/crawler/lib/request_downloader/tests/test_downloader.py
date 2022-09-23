import os
import sys
sys.path.append(os.getcwd())

from downloader_test import Request_Downloader, \
    Html_Request_Downloader, Browser_Downloader, Downloader_Manager


class TestDownloader():
    def test_request_downloader(self):
        rdownloader = Request_Downloader()
        result = rdownloader.get_html('https://dantri.com.vn')
        assert result is not None
        rdownloader.close()

    def test_browser_downloader(self):
        options = {
            "use_tor_proxy": True,
            "headless": True,
            "fast_load": True
        }

        firefox_downloader = Browser_Downloader(options)

        url = 'https://www.youtube.com/watch?v=ZNeurS5dPHo'
        script = 'return JSON.stringify(window["ytInitialData"]["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["richGridRenderer"]["contents"][0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"]);'
        timeout = 30
        script = None
        result = firefox_downloader.get_html(url, script=script, timeout=timeout, options={"debug": False})
        assert result is not None
        firefox_downloader.close()

    def test_html_request_downloader(self):
        html_downloader = Html_Request_Downloader(use_tor_proxy=True)
        url = 'https://www.youtube.com/watch?v=ZNeurS5dPHo'
        script = 'JSON.stringify(window["ytInitialData"]["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["richGridRenderer"]["contents"][0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"]);'
        timeout = 30
        result = html_downloader.get_html(url, render_javascript=True, script=script, timeout=timeout)
        assert result is not None
        html_downloader.close()

    def test_downloader_manager(self):
        options = {
            "headless": False
        }

        # get/create new downloader
        firefox_downloader = Downloader_Manager.request_downloader("Browser_Downloader", use_tor_proxy=True, options=options)
        url1 = 'https://www.youtube.com/watch?v=ZNeurS5dPHo'
        script = 'return JSON.stringify(window["ytInitialData"]["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["richGridRenderer"]["contents"][0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"]'
        timeout = 30
        if firefox_downloader:
            result = firefox_downloader.get_html(url1, script=script, timeout=timeout)
            print(f"Publish_date of {url1} is: {result}")

        # release downloader
        Downloader_Manager.release_downloader(firefox_downloader)

        # reuse the same downloader
        firefox_downloader = Downloader_Manager.request_downloader("Browser_Downloader", use_tor_proxy=True, options = options)
        if firefox_downloader:
            url2 = 'https://www.youtube.com/watch?v=0dLr9W5BDCA'
            script = 'return JSON.stringify(window["ytInitialData"]["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["richGridRenderer"]["contents"][0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"]'
            result = firefox_downloader.get_html(url2, script=script, timeout=timeout)
            print(f"Publish_date of {url2} is: {result}")

        Downloader_Manager.release_downloader(firefox_downloader)

        # test create 30 downloader at the same time
        for i in range(0, 10):
            print(f"Test request number {i}")
            firefox_downloader = Downloader_Manager.request_downloader("Browser_Downloader", use_tor_proxy=True, options = options)
            if firefox_downloader:
                url2 = 'https://www.youtube.com/watch?v=0dLr9W5BDCA'
                script = 'return JSON.stringify(window["ytInitialData"]["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["richGridRenderer"]["contents"][0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"]'
                result = firefox_downloader.get_html(url2, script=script, timeout=timeout)
                print(f"Publish_date of {url2} is: {result}")
            Downloader_Manager.release_downloader(firefox_downloader)

        assert True==True
        Downloader_Manager.close_all_downloader()

    def test_request_downloader_with_proxy(self):
        rdownloader = Request_Downloader(use_proxy=True)
        result = rdownloader.get_html('https://dantri.com.vn')
        assert result is not None
        rdownloader.close()

    def test_browser_downloader_with_proxy(self):
        options = {
            "base_dir": "/home/administrator/news_crawler_development/src/crawler/crawler/lib/request_downloader", 
            "use_tor_proxy": False,
            "use_proxy": True,
            "headless": True,
            "fast_load": True
        }

        firefox_downloader = Browser_Downloader(options)

        url = 'https://www.youtube.com/watch?v=ZNeurS5dPHo'
        script = 'return JSON.stringify(window["ytInitialData"]["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["richGridRenderer"]["contents"][0]["richItemRenderer"]["content"]["videoRenderer"]["publishedTimeText"]["simpleText"]);'
        timeout = 30
        script = None
        result = firefox_downloader.get_html(url, script=script, timeout=timeout, options={"debug": False})
        assert result is not None
        firefox_downloader.close()