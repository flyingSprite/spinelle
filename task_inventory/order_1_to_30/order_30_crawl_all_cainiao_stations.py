
"""Order 30: Crawl all cainiao stations

from url 'https://cart.taobao.com/cart.htm?spm=875.7931836%2FB.a2226mz.11.67fc5d461PCKtS&from=btop'
"""
import time
from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from scrapy import Selector
from scrapy.http import HtmlResponse
from pydispatch import dispatcher
import xlwt

# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
# 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器

fk = Faker()
dcap["phantomjs.page.settings.userAgent"] = fk.user_agent()
# 不载入图片，爬页面速度会快很多
dcap["phantomjs.page.settings.loadImages"] = False


class CrawlAllCainiaoStations(object):
    login_url = 'https://cart.taobao.com/cart.htm?spm=875.7931836%2FB.a2226mz.11.67fc5d461PCKtS&from=btop'
    chrome_driver_path = '/Users/Fernando/Develop/solutions/spinelle/static/drivers/chromedriver'
    browser = None
    button_more_id = 'J_LoadMore'
    prev_location = ''
    current_location = ''

    def __init__(self):
        super(CrawlAllCainiaoStations, self).__init__()

    def get_chrome_driver(self):
        return webdriver.Chrome(self.chrome_driver_path)

    def login(self):
        self.browser = self.get_chrome_driver()
        self.browser.get(self.login_url)
        self.switch_to_popup_iframe()

    def can_start_click_more(self):
        is_cannot_click_more = True
        while is_cannot_click_more:
            time.sleep(2)
            try:
                self.current_location = self.browser.find_element_by_id('J_AddressInput').get_attribute('value')
                print(self.current_location, self.prev_location)
                more_button = self.browser.find_element_by_id(self.button_more_id)
                if more_button.is_displayed():
                    is_cannot_click_more = False
                    self.repeat_click_more()
            except NoSuchElementException:
                pass
            if self.current_location != self.prev_location:
                time.sleep(2)
                is_cannot_click_more = False
                self.repeat_click_more()
            dispatcher.send(signal='loading')

    def switch_to_popup_iframe(self):
        is_loading_page = True
        while is_loading_page:
            try:
                iframe = self.browser.find_element_by_xpath("//div[@class='tc-popup-content']/iframe")
                self.browser.switch_to.frame(iframe)
                is_loading_page = False
                self.can_start_click_more()
            except NoSuchElementException:
                dispatcher.send(signal='loading')
                time.sleep(1)

    def repeat_click_more(self):

        can_click_more = True
        script = f'document.getElementById("{self.button_more_id}") && ' \
                 f'document.getElementById("{self.button_more_id}").click()'
        try:
            while can_click_more:
                self.browser.execute_script(script)
                time.sleep(3)
                button_more_ele = self.browser.find_element_by_id(self.button_more_id)
                if not button_more_ele.is_displayed():
                    can_click_more = False
        except NoSuchElementException:
            pass

        browser_response = HtmlResponse(
            self.login_url,
            encoding='utf-8',
            body=self.browser.page_source.encode('utf-8')
        )

        selector = Selector(browser_response)
        statation_uls = selector.xpath('//div[@id="J_StationMenu"]/ul')
        statation_list = list()
        for statation_ul in statation_uls:
            statation_info = statation_ul.xpath('.//p[@class="dai-full"]/text()').extract()
            statation_title = statation_ul.xpath('.//strong/text()').extract()
            if len(statation_info) == 2:
                title = statation_title[0]
                address = statation_info[0][3: len(statation_info[0])].strip()
                phone_number = statation_info[1][3: len(statation_info[1])].strip()
                statation_list.append({
                    'title': title,
                    'address': address,
                    'phone_number': phone_number
                })
        self.current_location = self.browser.find_element_by_id('J_AddressInput').get_attribute('value')
        self.prev_location = self.current_location
        dispatcher.send(signal='get_station_data', location=self.current_location, data=statation_list)
        dispatcher.send(signal='load_done_area')
        self.can_start_click_more()

    def regsitry_event(self, signal, func):
        if func and signal:
            dispatcher.connect(func, signal=signal, sender=dispatcher.Anonymous)


def call_loading():
    print('正在加载中。。。')


def call_load_done_area():
    print('加载完一个地区，请重新选中一个地区')


def write_excel_data(file_name, data):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('sheet 1')

    start_row_num = 0

    for row_id, row in enumerate(data):
        sheet.write(row_id + start_row_num, 0, row.get('title', ''))
        sheet.write(row_id + start_row_num, 1, row.get('address', ''))
        sheet.write(row_id + start_row_num, 2, row.get('phone_number', ''))

    workbook.save(file_name + '.xls')


def call_get_station_data(location, data):
    if data and len(data) > 0:
        write_excel_data(location, data)


statation = CrawlAllCainiaoStations()
statation.regsitry_event('loading', call_loading)
statation.regsitry_event('load_done_area', call_load_done_area)
statation.regsitry_event('get_station_data', call_get_station_data)

statation.login()

