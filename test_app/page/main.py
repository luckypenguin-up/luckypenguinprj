from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_app.page.search import Search

#
class Main:
    _driver: WebDriver #存放driver的对象
    def __init__(self,driver):#接受app的driver方法
        self._driver = driver

    def goto_search(self):
        self._driver.find_element(MobileBy.ID, "tv_search").click()
        return Search(self._driver)