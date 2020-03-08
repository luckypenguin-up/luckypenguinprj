
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_app.page.base_page import BasePage


class Search(BasePage):
    #todo: 多平台、多版本、多个定位符
    _name_locator = (MobileBy.ID, "name")
    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        #改造 兼容多平台的定位符 element = (MobileBy.ID, "name")
        self.find(self._name_locator).click()
        return self

    def market_search(self,key):
        self.find(MobileBy.ID, "action_search").click()
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(self._name_locator).click()
        return self

    def market_search_back(self):
        self.find(MobileBy.ID, "action_close").click()

    def get_price(self, key: str) -> float:
        element = (MobileBy.ID,"current_price")
        return float(self.find(element).text)

    def add_select(self):#666 get it
        element = self.find_by_text("加自选")
        element.click()
        return self

    def un_select(self):
        element = self.find_by_text("已添加")
        element.click()
        return self
    def get_msg(self):
        return self.find(By.ID, "followed_btn").text