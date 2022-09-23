"""
This module provide downloader class. These are:
    Request_Downloader: use request lib to crawl normal page
    Browser_Downloader: use firefox with selenium to crawl AJAX page
        - profile: load firefox profile (use for bot login)
    Html_Request_Downloader: use Chromium through html_requests to crawl normal page & render javascript
    Additional: use tor as proxy

This module also provide Downloader_Manager class to manage assigning downloader (avoid instantiating too many downloader --> memory leak). Important function:
    - request_downloader(): get downloader
    - release_downloader(): release downloader for reusing by another request
    - close_all_downloader(): close all downloader. Note: this function is called automatically to avoid memory leak
"""

import os
import sys
sys.path.append(os.getcwd())

from fake_useragent import UserAgent
import logging
import requests
import requests_html
import random
import re
from .tor_proxy import TorManager
from .proxy import apply_proxy, apply_proxy_for_firefox
from selenium import webdriver
import selenium.webdriver.firefox
import selenium.webdriver.chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time
import datetime
import traceback


# UTILITY FUNCTION
def print_exception():
    # Print error message in try..exception
    exec_info = sys.exc_info()
    traceback.print_exception(*exec_info)

# MAIN CLASS
class Downloader_Manager():
    """Manage all running downloader of a task"""
    # NOTE:
    # running_download is class static variable, used to manage running
    # Browser_Downloader. But this can't be used across Celery.task
    # (each Celery.task has its own version of running_download)

    # running_downloader = {'downloader': , 'count': int}
    #   downloader: Downloader obj
    #   count     : count number this downloader is assisgned
    running_downloader = []
    max_downloader = {
            'Browser_Downloader': 2,
            'Html_Request_Downloader': 2,
            'Request_Downloader': 100000
        }
    is_blocked = False
    block_date = None

    @staticmethod
    def report_being_blocked():
        """Stop provide any downloader for 5 minute"""
        Downloader_Manager.is_blocked = True
        Downloader_Manager.block_date = time.now()

    @staticmethod
    def check_if_unblocked():
        if Downloader_Manager.is_blocked:
            now = datetime.now()
            if (now - Downloader_Manager.block_date).total_seconds() > 600: # 10 minute has passed
                Downloader_Manager.is_blocked = False
                return True
            else:
                return False
        else:
            return True
    @staticmethod
    def count_downloader(downloader_type):
        count = 0
        for downloader in Downloader_Manager.running_downloader:
            if downloader['downloader_type'] == downloader_type:
                count += 1
        return count

    @staticmethod
    def close_all_downloader():
        for downloader in Downloader_Manager.running_downloader:
            downloader['downloader'].close()
        Downloader_Manager.running_downloader = []

    @staticmethod
    def provide_available_downloader(downloader_type, use_tor_proxy=False, use_proxy=False, profile=None, options=None):
        """Check if any downloader is available"""
        """
            args:
                use_tor_proxy
                profile: None - no specify profile
                       : str  - must be this profile
        """
        if Downloader_Manager.running_downloader:
            random.shuffle(Downloader_Manager.running_downloader)
            for downloader in Downloader_Manager.running_downloader:
                if downloader['downloader_type'] == downloader_type and downloader['free']:

                    if profile: # check profile criteria
                        if 'profile' in downloader:
                            if downloader['profile'] != profile:
                                # time.sleep(20) # use the same bot. Slow down
                                continue

                    if options:
                        if 'options' in downloader:
                            if downloader['options'] != options:
                                continue

                    downloader['free'] = False
                    return downloader['downloader']
        return False

    @staticmethod
    def release_downloader(downloader):
        """Release downloader so that other task can use"""
        if downloader:
            for running_downloader in Downloader_Manager.running_downloader:
                if downloader == running_downloader['downloader']:
                    running_downloader['free'] = True


    @staticmethod
    def request_downloader(downloader_type, use_tor_proxy=False, use_proxy=False, profile=None, options=None, timeout=60):
        """Check if request downloader is avail and provide for crawler"""
        """
            args:
                downloader_type: str in ['Request_Downloader',
                                         'Browser_Downloader',
                                         'Html_Request_Downloader']
                use_tor_proxy
                use_proxy: use proxy from proxy list 
                profile (for Firefox Browser only)
                timeout: max time to wait until get a available downloader
            return:
                Downloader instance if can recycle or can create a new one
                False if need to wait some time (for recycling old downloader)
                None if can't get downloader
        """
        # Explain:
        # request_downloader does some tasks:
        # 1. It decided whether to recycle a running Download_Browser
        # or create a new one (a new one will help balance load but consume
        # more resources)
        # 2. If create a new one, it choose randomly a bot profile to
        # prevent bots from being banned
        #   If can't create a new one (memory is full for example), It will wait until can create an available or timeout
        # 3. If can't recyle or create a new downloader. It will wait until get an available downloader or timeout

        if not Downloader_Manager.check_if_unblocked():
            print("Being blocked. Can't provide new downloader")
            return None

        if downloader_type == "Request_Downloader":
            downloader =  Request_Downloader(use_proxy=use_proxy, use_tor_proxy=use_tor_proxy)
            logging.info("Successfully provide a new Request_Downloader")
            return downloader
        elif downloader_type == "Html_Request_Downloader":
            downloader = Downloader_Manager.provide_available_downloader(downloader_type, use_tor_proxy, use_proxy, profile, options)
            if downloader:
                return downloader
            else:
                # can not recycle or no available downloader
                if Downloader_Manager.count_downloader(downloader_type) < Downloader_Manager.max_downloader[downloader_type]:
                    downloader = Html_Request_Downloader(use_tor_proxy=use_tor_proxy)
                    if downloader and downloader.is_alive():
                        Downloader_Manager.running_downloader.append({
                            'downloader_type': downloader_type,
                            'downloader': downloader,
                            'free': False,
                            'profile': None
                        })
                        return downloader
                    else:
                        print("Can't create new Downloader now")
                        return None
                else:
                    if timeout > 0:
                        time_count = 0
                        time_step = 15
                        downloader = None
                        while (time_count < timeout) and (not downloader):
                            time.sleep(time_step)
                            logging.info("Wait for available downloader")
                            time_count += time_step

                            downloader = Downloader_Manager.request_downloader(downloader_type, use_tor_proxy=use_tor_proxy, use_proxy=use_proxy, timeout=0)

                        if not downloader:
                            logging.info("Can't create more Browser_Downloader now ")

                        return downloader
                    else:
                        return None

            logging.info("Successfully provide a new Html_Request_Downloader")
            return downloader
        elif downloader_type == "Browser_Downloader":
            downloader = Downloader_Manager.provide_available_downloader(downloader_type, use_tor_proxy, use_proxy, profile)
            if downloader:
                return downloader
            else:
                # can not recycle or no available downloader
                if Downloader_Manager.count_downloader(downloader_type) < Downloader_Manager.max_downloader[downloader_type]:
                    if not options:
                        options = {}
                        options['use_tor_proxy'] = use_tor_proxy,
                        options['use_proxy'] = use_proxy,
                        options['profile']: profile

                    downloader = Browser_Downloader(options)
                    if downloader and downloader.is_alive():
                        new_profile = downloader.get_profile()
                        Downloader_Manager.running_downloader.append({
                            'downloader_type': downloader_type,
                            'downloader': downloader,
                            'free': False,
                            'profile': new_profile
                        })
                        return downloader
                    else:
                        logging.error("Can not create new Browser_Downloader now")
                        return None
                else:
                    if timeout > 0:
                        time_count = 0
                        time_step = 15
                        downloader = None
                        while (time_count < timeout) and (not downloader):
                            logging.info("Wait for available downloader")
                            time.sleep(time_step)
                            time_count += time_step
                            downloader = Downloader_Manager.request_downloader(downloader_type, use_tor_proxy=use_tor_proxy, use_proxy=use_proxy, timeout=0)

                        if not downloader:
                            logging.info("Can't create more Browser_Downloader now ")

                        return downloader

                    else:
                        return None
        else:
            logging.error(f"Do not know downloader type {downloader_type}")
            return None
        logging.error("Can not provide a new Browser_Downloader")
        return None

# DOWNLOADER CLASSES

class Abstract_Auto_Managed_Downloader():
    """Abstract class for all downloader"""
    """
        Auto_Managed means:
        - auto detect when downloader is over-used (can lead to ban bot account)
        - auto reload new bot account
    """

    def __init__(self):
        """init tasks go here"""
        pass

    # control driver function
    def click(self, selector):
        pass

    def get_html(self, url, options={}):
        """return html from site in url"""
        """
        args:
            url: link (string)
            options: dicts contain options
        """

    def close(self):
        """finish tasks go here"""

    def reload(self):
        """Reload downloader when over-used"""


class Request_Downloader(Abstract_Auto_Managed_Downloader):
    """Downloader that use requests lib"""

    def __init__(self, use_tor_proxy=False, use_proxy=False):
        """init tasks go here"""
        self.session = requests.Session()
        self._use_tor_proxy = use_tor_proxy
        self._use_proxy = use_proxy

        if use_tor_proxy:
            TorManager().apply_tor_proxy(self.session)

        if use_proxy:
            apply_proxy(self.session)


    def get_html(self, url, options={}):
        """return html from site in url"""
        """
        args:
            url: link (string)
            options: dicts contain options
                - 'timeout': timeout in seconds
        return:
            html or None
        """
        timeout = 60 if 'timeout' not in options else options['timeout']

        user_agent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36'

        hdr = {
        	'user-agent': user_agent,
        	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        	'accept-charset': 'utf-8;q=0.7,*;q=0.3',
        	'accept-encoding': 'none',
        	'accept-language': 'en-us,en;vi;q=0.8',
        	'connection': 'keep-alive'
		}

        try:
            if self._use_tor_proxy:
                response = self.session.get(url, headers=hdr, timeout=timeout)
            else:
                response = requests.get(url, headers=hdr, timeout=timeout)

            if response.status_code == 200:
                if response.encoding=='ISO-8859-1':
                    html_source = response.content.decode('utf-8')
                else:
                    html_source = response.text
                return html_source
            else:
                logging.info(f"Request_Downloader can't get_html from {url}")
                return None
        except:
            print_exception()


    def reset_tor_proxy(self):
        """Reset Tor Proxy to get a new IP"""
        TorManager().reset_tor_IP()


    def reload(self):
        """Reinit with the same option"""
        self.__init__(use_tor_proxy=self.use_tor_proxy)


    def close(self):
        """finish tasks go here"""
        try:
            if self.session:
                self.session.close()
        except:
            logging.error("Request_Downloader can't close its session. It might cause memory leak !!!")
            # print_exception()


class Html_Request_Downloader(Abstract_Auto_Managed_Downloader):
    """Downloader that use Chromium through html_request lib"""
    """
        How to use: init it with use_tor_proxy = True to use Tor Proxy for request
            - get_html(url, render_javascript, script): to get html from url, render/run javascript or not
    """
    session = None # this represent HTMLSession instance
    use_tor_proxy = False
    max_request = 100 # number of request to restart chromium

    def __init__(self, use_tor_proxy=False):
        """init tasks go here"""
        self.session = requests_html.HTMLSession()
        if use_tor_proxy:
            self.use_tor_proxy = use_tor_proxy
            TorManager().apply_tor_proxy(self.session)

        # set initial count
        self.request_count = 0


    def _render_url(self, session, url, render_javascript, script, timeout, headers=None) :
        """Get html, render ajax or run javascript command"""
        """
            Args:
                - render_javascript: render Ajax or not
                - script: javascript command to run (render_javascript must be True)
            Return:
                (result, status_code)
        """
        try:
            # check if max_request is got
            if self.request_count <= self.max_request:
                logging.info("Html_Request_Downloader max_request has been passed. Reload")
                self.reload() # reset

            result = session.get(url, timeout=timeout, headers=headers)
            if result.status_code == 200: # OK
                html = result.content.decode("utf-8")

                if render_javascript:
                    html = str(result.html.render(script=script, timeout=timeout))
                    return html, result.status_code
                else:
                    return html, result.status_code
            else:
                return None, result.status_code
        except:
            # print_exception()
            logging.error(f"HTML_Request_Downloader has error while get/rendering {url}")
            return None, None


    def is_alive(self):
        """Check if this downloader is working"""
        return True

    def get_html(self, url, render_javascript=False, script=None, timeout=60):
        """return html from site in url"""
        """
        args:
            url: link (string)
            render_javascript: render AJAX or not
            script: javascript to run
        """

        try:
            session = self.session
            response = session.get(url, timeout=timeout)
            result, status_code = self._render_url(session, url, render_javascript, script, timeout)

            if status_code == 200:
                return result
            elif response.status_code == 421: # too many request
                if self.use_tor_proxy:
                    self.reset_tor_proxy()
                    self.reload()
                    return self._render_url(session, url, render_javascript, script, timeout)
                else:
                    logging.info(f"HTML_Request_Downloader get too many requests status_code. Should you Tor Proxy to change IP")
                    return None
            else:
                logging.info(f"HTML_Request_Downloader can't get_html from {url}")
                return None
        except:
            print_exception()
            logging.error(f"HTML_Request_Downloader break while calling get_html from {url}")


    def reset_tor_proxy(self):
        """Reset Tor Proxy to get a new IP"""
        TorManager().reset_tor_IP()


    def reload(self):
        """Reinit with the same option"""
        self.__init__(use_tor_proxy=self.use_tor_proxy)


    def close(self):
        """finish tasks go here"""
        try:
            if self.session:
                self.session.close()
        except:
            logging.error("HTML_Request_Downloader can't close its session. It might cause memory leak !!!")
            # print_exception()


class Browser_Downloader(Abstract_Auto_Managed_Downloader):
    """Downloader that use browser with selenium lib"""
    """
        Typical Use:
            br = Browser_Downloader({}) # create a headless, firefox instance
            br.get_html(url, {})# return html of page url
            br.close()          # close
    """

    def __init__(self, options):
        """
            args:
                options: dicts contain options
                - 'browser': Firefox/Chrome..
                - 'use_tor_proxy': True/False
                - 'use_proxy': True/False
                - 'timeout': timeout in seconds
                - 'headless': True/False
                - 'fast_load': True/False
                - 'random_profile': True/False
                - 'profile': profile_name (browser profile, saved in profiles folder)
                    + None: no use profile
                    + True: use default / random profile
                    + str: use this profile
                - 'max_activities': int # number of activities (get_url, click) to be
                                    considered over-used
        """
        self._options = options
        self._browser = None
        self.create(recreate=False)


    def _get_Firefox_profile(self, profile):
        """Return Firefox profile"""
        """
            args:
                - profile: profile name (Firefox profile are saved in profiles dir)
            return FirefoxProfile instance
        """
        if profile:
            profile_path = os.getcwd() + f"/profiles/{profile}"

            if os.path.isdir(profile_path):
                return webdriver.FirefoxProfile(profile_path)
            else:
                logging.error(f"Profile {profile} does not exist."
                              f"Must create profile {profile} with setup_browser.py first")
                return None
        else:
            logging.error("get_Firefox_profile: profile can not be None")
            return None


    def is_alive(self):
        """Check if this downloader is working"""
        return self._browser

    def create(self, recreate=False):
        """Create browser instance """
        """
        return:
            browser instance if success
            False if failed
        """
        # parse options
        options = self._options
        self._activities = 0
        base_dir = '' if 'base_dir' not in options else options['base_dir'] #path to request_downloader lib folder. It need to locate adblock extension file
        browser = "Firefox" if 'browser' not in options else options['browser']
        fast_load = False if 'fast_load' not in options else options['fast_load']
        headless = True if 'headless' not in options else options['headless']
        self._max_activities = 50 if 'max_activities' not in options else options['max_activities']
        profile = None if 'profile' not in options else options['profile']
        random_profile = False if 'random_profile' not in options else options['random_profile']
        timeout = 60 if 'timeout' not in options else options['timeout']
        use_tor_proxy = False if 'use_tor_proxy' not in options else options['use_tor_proxy']
        use_proxy = False if 'use_proxy' not in options else options['use_proxy']
        binary_location = None if 'binary_location' not in options else options['binary_location']
        driver_path = None if 'driver_path' not in options else options['driver_path']
        
        # create browser instance
        if browser=="Firefox":
            """Start Firefox Browser with options"""
            firefox_options = selenium.webdriver.firefox.options.Options()

            if headless:
                firefox_options.add_argument("--headless")

            if profile:
                if recreate:
                    time.sleep(3) # stop crawling to protect bots
                browser_profile = self._get_Firefox_profile(profile)
                self._profile = profile
            else:
                if random_profile:
                    profile_name =  self._get_random_profile()
                    self._profile = profile_name
                    browser_profile = self._get_Firefox_profile(profile_name)
                else:
                    browser_profile = webdriver.FirefoxProfile()
                    self._profile = 'default'

            if fast_load:
                # Disable CSS
                browser_profile.set_preference('permissions.default.stylesheet', 2)
                # Disable images
                browser_profile.set_preference('permissions.default.image', 2)
                # Disable notification
                browser_profile.set_preference('permissions.default.desktop-notification', 2)
                # Disable Flash
                browser_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
                # Adblock Extension
                browser_profile.exp = base_dir + "/resource/adblock.xpi"
                browser_profile.add_extension(extension=browser_profile.exp)

            if use_tor_proxy:
                TorManager().apply_tor_proxy_for_firefox(browser_profile)

            if use_proxy: 
                apply_proxy_for_firefox(browser_profile)

            # explain:
            # sometimes, geckodriver can't not create new Firefox instance
            retry = 0
            driver = None
            while retry < 2:
                try:
                    driver = webdriver.Firefox(options=firefox_options, firefox_profile=browser_profile)
                    break
                except:
                    print("Retry to create new Firefox instance")
                    # print_exception()
                    retry += 1
                    time.sleep(2)

            if driver:
                # set browser timeout
                driver.set_page_load_timeout(timeout)

                # save browser instance in class property
                self._browser = driver
                return driver
            else:
                self._browser = None
                logging.error(f'Browser_Downloader can not create new Firefox instance')
                return False

        elif browser=="Brave":
            """Start Brave Browser with options"""
            browser_options = selenium.webdriver.chrome.options.Options()
            #browser_options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
            #driver_path = '/usr/local/bin/chromedriver'
            browser_options.binary_location = binary_location
            
            if headless:
                browser_options.add_argument("--headless")

            if profile:
                if recreate:
                    time.sleep(3) # stop crawling to protect bots
                browser_profile = self._get_Firefox_profile(profile)
                self._profile = profile
            else:
                if random_profile:
                    profile_name =  self._get_random_profile()
                    self._profile = profile_name
                    browser_profile = self._get_Firefox_profile(profile_name)
                else:
                    browser_profile = webdriver.FirefoxProfile()
                    self._profile = 'default'

            if fast_load:
                # Disable CSS
                browser_profile.set_preference('permissions.default.stylesheet', 2)
                # Disable images
                browser_profile.set_preference('permissions.default.image', 2)
                # Disable notification
                browser_profile.set_preference('permissions.default.desktop-notification', 2)
                # Disable Flash
                browser_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
                # Adblock Extension
                browser_profile.exp = base_dir + "/resource/adblock.xpi"
                browser_profile.add_extension(extension=browser_profile.exp)

            if use_tor_proxy:
                TorManager().apply_tor_proxy_for_firefox(browser_profile)

            if use_proxy: 
                apply_proxy_for_firefox(browser_profile)

            # explain:
            # sometimes, geckodriver can't not create new Firefox instance
            retry = 0
            driver = None
            while retry < 2:
                try:
                    driver = webdriver.Chrome(options=browser_options, executable_path=driver_path)
                    break
                except:
                    print("Retry to create new Brave instance")
                    print_exception()
                    retry += 1
                    time.sleep(2)

            if driver:
                # set browser timeout
                driver.set_page_load_timeout(timeout)

                # save browser instance in class property
                self._browser = driver
                return driver
            else:
                self._browser = None
                logging.error(f'Browser_Downloader can not create new Brave instance')
                return False

    def scroll_to_view(self, selector):
        """Control browser to focus on an item before click or do smth"""
        """
            args:
                selector: xpath to select item
            return:
                True if success
                False if error
        """
        try:
            # element = self._browser.find_element_by_xpath(selector)
            element = WebDriverWait(self._browser, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
            # # try to scroll in to view
            action = ActionChains(self._browser)
            action.move_to_element(element)
            action.pause(1)
            action.perform()
            return True
        except:
            # print_exception()
            logging.error(f"Browser_Downloader: can not scroll to element {selector}")
            return False


    def click(self, selector):
        """Control browser to click on an item"""
        """
            args:
                selector: xpath to select item
            return:
                True if success
                False if error
        """
        self._activities += 1

        try:
            element = self._browser.find_element_by_xpath(selector)
            element.click()
            return True
        except:
            # print_exception()
            logging.error(f"Browser_Downloader: can not click on element {selector}")
            return False

    def close(self):
        """Close current tab"""
        if self._browser is not None:
            # explain
            # if browser has been closed. This will make exception ("execute command
            # without connection")
            try:
                self._browser.close()
            except:
                pass
            logging.info("Browser_Downloader has closed browser instance successfuly")
        else:
            logging.error("Browser_Downloader has been terminated before calling close()")


    def execute_javascript(self, javascript):
        """Execute javascript commands"""
        """
            args:
            return
                Value if success
                False if failed
        """
        try:
            result = self._browser.execute_script(javascript)
            return result
        except:
            # print_exception()
            logging.error(f"Browser Downloader have error when executing javasciprt {javascript}")
            return False


    def execute(self, commands=[], script=None):
        """Control browser with commands or script file"""
        """
            args:
            return:
                True if success
                False if failed
        """
        return True

    def get_current_url(self):
        """Get current url"""
        """
            return: url if success. None if fail
        """
        try:
            return str(self._browser.current_url)
        except:
            return None


    def _get_random_profile(self):
        """Get all available Browser profile"""
        """
            return: profile_name (str)
        """
        profiles = []
        try:
            profiles = os.listdir('profiles')
            if profiles:
                # explain
                # avoid '.git' profile
                profile = '.git'
                while profile.strip() == '.git':
                    profile = random.choice(profiles)
                return profile
            else:
                return None
        except:
            logging.error("Can't find profiles folders")
            return None


    def get_html(self, url, script=None, timeout=60, options={}):
        """return html from site in url"""
        """
        args:
            url: link (string)
            script: javascript to run after get html
            options: dicts contain options
                - 'pre_wait': sleep pre_wait second to wait for full pageload
                - 'pre_commands': [] of command to execute before get_html
                - 'pre_script': script file to execute before get_html
                - 'pos_commands': [] of command to execute after get_html
                - 'pos_script': script file to execute after get_html
                - 'debug': print debug information
        return:
            Ok: html
            False: this downloader have error
            None: can't get data

       """
        self._activities += 1
        if self.over_used():
            self.close()
            new_downloader = self.create(recreate=True)
            if new_downloader:
                return self.get_html(url, script, timeout, options)
            else:
                logging.error("Browser_Downloader: can not recreate downloader")
                return None

        # parse options
        pre_wait = 0 if 'pre_wait' not in options else options['pre_wait']
        pre_commands = [] if 'pre_commands' not in options else options['pre_commands']
        pre_script = None if 'pre_script' not in options else options['pre_script']
        pos_commands = [] if 'pos_commands' not in options else options['pos_commands']
        pos_script = None if 'pos_script' not in options else options['pos_script']
        debug = False if 'debug' not in options else options['debug']

        # open browser
        if not self._browser: # this browser can't be created
            return False

        browser = self._browser
        try:
            # load page

            # eplain:
            # sometime geckodrive can create new Firefox instance but error on
            # get url. So we need to retry here
            retry = 0
            while retry <2:
                try:
                    browser.get(url)
                    break
                except:
                    if debug:
                        print("Get error on get(url). Retry")
                    retry+=1
                    time.sleep(2)

            # wait for full load
            time.sleep(pre_wait)

            # run pre_commands
            success = self.execute(pre_commands, pre_script)
            if not success:
                logging.error("Browser_Downloader can not run pre_commands/script")
                return None

            # get html
            html = browser.page_source
            if debug:
                print(f"Page source of {url}: ")
                print(html)

            # run pos_commands
            success = self.execute(pos_commands, pos_script)

            # execute javascript
            if script:
                try:
                    script_result = self.execute_javascript(script)
                    if not script_result and 'return' not in script:
                        print("Javascript run without returning value. You should add return to script string !")
                    return script_result
                except:
                    # print_exception()
                    print(f"Browser_Downloader can't execute script {script}")
                    return None

            # return html
            logging.info(f"Browser_Downloader successfuly get_html from {url}")
            return html

        except:
            logging.error(f"Browser_Downloader can not get_html from {url}")
            # print_exception()
            return None

    def get_profile(self):
        return self._profile

    def get_page_source(self):
        """get pagesoure of current page"""
        """
            args:
                return html pagesource if success
                return None if fail
        """
        try:
            return self._browser.page_source
        except:
            logging.error("Browser_Downloader.get_page_source: can not get html"
                          "pagesource")
            return None

    def modify_url(self, selector, replacer):
        """Modify current url using regular expression"""
        """
            args:
                selector: selector regex
                replacer: replacer string
        """
        try:
            current_url = self.get_current_url()
            selector_regex = re.compile(str(selector))
            # logging.error(current_url)
            # logging.error(selector_regex)
            # logging.error(replacer)
            new_url = re.sub(selector_regex, str(replacer), current_url)
            if new_url != current_url:
                self._browser.get(new_url) # move to new url
            return True
        except:
            # print_exception()
            return None

    def switch_to_default(self):
        """Switch current context to default iframe"""
        """
            return:
                True if success, None if fail
        """
        try:
            self._browser.switch_to.default_content()
            return True
        except:
            # print_exception()
            logging.error("switch_to_iframe: can not switch to default frame")
            return None

    def switch_to_iframe(self, iframe_xpath=""):
        """Switch current context to iframe"""
        """
            args: iframe_xpath: xpath to get iframe element
            return:
                True if success, None if fail
        """
        try:
            iframe = self._browser.find_element_by_xpath(iframe_xpath)
            self._browser.switch_to_frame(iframe)
            return True
        except:
            # print_exception()
            logging.error(f"switch_to_iframe: can not switch to {iframe_xpath}")
            return None

    def switch_to_parent(self):
        """Switch current context to parent iframe"""
        """
            return:
                True if success, None if fail
        """
        try:
            self._browser.switch_to.parent_frame()
            return True
        except:
            # print_exception()
            logging.error("switch_to_iframe: can not switch to parent frame")
            return None


    def over_used(self):
        return self._activities > self._max_activities

    def quit(self):
        """Real quit here"""
        if self._browser is not None:
            try:
                self._browser.quit()
                logging.info("Browser_Downloader has quited browser instance successfuly")
            except:
                logging.error("Browser_Downloader can't quit")
                pass
        else:
            logging.error("Browser_Downloader has been terminated before calling close()")


# Below code is to ensure that Downoad_Manager.close_all_downloader is called when process restart
import atexit
atexit.register(Downloader_Manager.close_all_downloader)



