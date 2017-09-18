
"""Order 30: Crawl all cainiao stations

Login URL: https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fdelivery.tmall.com%2Fstation%2FshowStationInPopup.htm%3FareaId%3D110105%26addressId%3D7488193372%26serviceType%3D101%26appName%3Dtmall%26t%3D1505186126935%26lgBuyAddId%3D1951961267%26stationId%3D140915
"""
import time
from faker import Faker
from selenium import webdriver
# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器

fk = Faker()
dcap["phantomjs.page.settings.userAgent"] = fk.user_agent()
# 不载入图片，爬页面速度会快很多
dcap["phantomjs.page.settings.loadImages"] = False



class CrawlAllCainiaoStations(object):
    phantomjs_driver_path = 'D:/dev/Solution/spinelle/static/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs.exe'
    login_url = 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fdelivery.tmall.com%2Fstation%2FshowStationInPopup.htm%3FareaId%3D110105%26addressId%3D7488193372%26serviceType%3D101%26appName%3Dtmall%26t%3D1505186126935%26lgBuyAddId%3D1951961267%26stationId%3D140915'
    firefox_path = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'

    chrome_driver_path = 'D:/dev/Solution/spinelle/static/drivers/chromedriver-v2.32.exe'
    firefox_driver_path = 'D:/dev/Solution/spinelle/static/drivers/geckodriver-v0.18.0.exe'

    def __init__(self):
        pass

    def get_firefox_driver(self):
        return webdriver.Chrome(executable_path=self.firefox_driver_path)

    def get_chrome_driver(self):
        return webdriver.Chrome(self.chrome_driver_path)

    def login(self):
        browser = self.get_chrome_driver()

        browser.get(self.login_url)
        time.sleep(20)
        print(browser.title)

        # $('#J_LoadMore')


l = CrawlAllCainiaoStations()
l.login()
