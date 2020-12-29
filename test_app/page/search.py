
from appium.webdriver.common.mobileby import MobileBy
from djcelery.admin_utils import action
from selenium.webdriver.common.by import By

from test_app.page.base_page import BasePage


class Search(BasePage):
    #todo: 多平台、多版本、多个定位符
    _name_locator = (MobileBy.ID, "name")
    def search(self, key: str):
        self.find(By.XPATH,"//*[contains(@class,'androidx.appcompat.widget.LinearLayoutCompat')]").click()
        self.find(MobileBy.ID, "ocet_edit").send_keys(key)
        self._driver.execute_script("mobile:performEditorAction", {"action": "search"})
        #改造 兼容多平台的定位符 element = (MobileBy.ID, "name")
       #self.find(self._name_locator).click()
        return self

    def market_search(self, key):
        self.find(MobileBy.ID, "action_search").click()
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(self._name_locator).click()
        return self

    def market_search_back(self):
        self.find(MobileBy.ID, "action_close").click()

    def get_address(self):
        element = (By.XPATH, "//*[contains(@resource-id,'tv_box_address')]")
        return self.find(element).text

    def add_select(self):#666 get it
        element = self.find_by_text("收藏")
        element.click()
        return self

    def un_select(self):
        element = self.find_by_text("已收藏")
        element.click()
        return self
    def get_msg(self):
        return self.find(By.ID, "tv_collection_text").text