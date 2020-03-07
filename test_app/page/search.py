import string

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class Search:
    _driver: WebDriver  # 存放driver的对象

    def __init__(self, driver):  # 接受app的driver方法
        self._driver = driver
    def search(self, key: str):
        self._driver.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        self._driver.find_element(MobileBy.ID, "name").click()
        return self

    def get_price(self, key: str) -> float:
        return float(self._driver.find_element(MobileBy.ID,"current_price").text)