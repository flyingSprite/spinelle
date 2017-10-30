
"""Order 30: Crawl all cainiao stations

Login URL: https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fdelivery.tmall.com%2Fstation%2FshowStationInPopup.htm%3FareaId%3D110105%26addressId%3D7488193372%26serviceType%3D101%26appName%3Dtmall%26t%3D1505186126935%26lgBuyAddId%3D1951961267%26stationId%3D140915
"""
import time
from faker import Faker
from selenium import webdriver
from scrapy import Selector
from scrapy.http import HtmlResponse
from common.utility.selenum_utility import Driver
from selenium.webdriver.remote.webelement import WebElement
# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器

fk = Faker()
dcap["phantomjs.page.settings.userAgent"] = fk.user_agent()
# 不载入图片，爬页面速度会快很多
dcap["phantomjs.page.settings.loadImages"] = False


class CrawlAllCainiaoStations(Driver):
    phantomjs_driver_path = 'D:/dev/Solution/spinelle/static/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs.exe'
    login_url = 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fdelivery.tmall.com%2Fstation%2FshowStationInPopup.htm%3FareaId%3D110105%26addressId%3D7488193372%26serviceType%3D101%26appName%3Dtmall%26t%3D1505186126935%26lgBuyAddId%3D1951961267%26stationId%3D140915'
    firefox_path = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'

    # chrome_driver_path = 'D:/dev/Solution/spinelle/static/drivers/chromedriver-v2.32.exe'
    chrome_driver_path = '/Users/Fernando/Develop/solutions/spinelle/static/drivers/chromedriver'
    firefox_driver_path = 'D:/dev/Solution/spinelle/static/drivers/geckodriver-v0.18.0.exe'
    browser = None

    def __init__(self):
        super(CrawlAllCainiaoStations, self).__init__()

    def get_firefox_driver(self):
        return webdriver.Chrome(executable_path=self.firefox_driver_path)

    def get_chrome_driver(self):
        return webdriver.Chrome(self.chrome_driver_path)

    def login(self):
        self.browser = self.get_chrome_driver()
        # self.login_url = 'http://oversea.huanqiu.com/'
        self.browser.get(self.login_url)
        # time.sleep(2)
        # browser_response = HtmlResponse(
        #     self.login_url,
        #     encoding='utf-8',
        #     body=browser.page_source.encode('utf-8')
        # )
        # sel = Selector(browser_response)
        # lis = sel.xpath('//ul[@name="contentList"]/li')
        # print(lis.extract())
        # for li in lis:
        #     print(li.xpath('.//h3/text()').extract())

        time.sleep(30)
        self.start_crawl_stations()

    def start_crawl_stations(self):

        while True:
            self.repeat_click_more()
            print('你有20秒的时间选择另外一个区：')
            time.sleep(10)
            print('还剩10秒')
            time.sleep(5)
            print('还剩5秒')
            time.sleep(1)
            print('还剩4秒')
            time.sleep(1)
            print('还剩3秒')
            time.sleep(1)
            print('还剩2秒')
            time.sleep(1)
            print('还剩1秒')

    def repeat_click_more(self):
        button_more_id = 'J_LoadMore'
        can_click_more = True
        while can_click_more:
            self.browser.execute_script(
                f'document.getElementById("{button_more_id}") && document.getElementById("{button_more_id}").click()')
            time.sleep(3)
            button_more_ele = self.browser.find_element_by_id(button_more_id)
            print(button_more_ele.text, button_more_ele.get_attribute('style'))
            if 'display: none;' in button_more_ele.get_attribute('style'):
                can_click_more = False

        print('crawl end ....')

        browser_response = HtmlResponse(
            self.login_url,
            encoding='utf-8',
            body=self.browser.page_source.encode('utf-8')
        )

        selector = Selector(browser_response)
        statation_uls = selector.xpath('//div[@id="J_StationMenu"]/ul')
        for statation_ul in statation_uls:
            statation_info = statation_ul.xpath('.//p[@class="dai-full"]/text()').extract()
            statation_title = statation_ul.xpath('.//strong/text()').extract()
            if len(statation_info) == 2:
                title = statation_title[0]
                address = statation_info[0][3: len(statation_info[0])].strip()
                phone_number = statation_info[1][3: len(statation_info[1])].strip()
                print(title, address, phone_number)


statation = CrawlAllCainiaoStations()
statation.login()
