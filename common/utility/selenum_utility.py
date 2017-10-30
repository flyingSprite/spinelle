from selenium import webdriver


class Driver(object):
    # chrome_driver_path = 'D:/dev/Solution/spinelle/static/drivers/chromedriver-v2.32.exe'
    chrome_driver_path = '/Users/Fernando/Develop/solutions/spinelle/static/drivers/chromedriver'
    firefox_driver_path = 'D:/dev/Solution/spinelle/static/drivers/geckodriver-v0.18.0.exe'

    def __init__(self):
        pass

    def get_firefox_driver(self):
        return webdriver.Chrome(executable_path=self.firefox_driver_path)

    def get_chrome_driver(self):
        return webdriver.Chrome(self.chrome_driver_path)