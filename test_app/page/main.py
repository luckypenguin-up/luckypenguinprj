from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_app.page.base_page import BasePage
from test_app.page.profile import Profile
from test_app.page.search import Search


class Main(BasePage):
    def goto_search(self):
        element = (By.XPATH, "//*[contains(@text, '空箱查询')]")
        self.find(element).click()
        return Search(self._driver)

    def goto_profile(self):
        self.find(By.XPATH, '//*[@text="我的" and contains(@resource-id,"tab_name")]').click()
        return Profile(self._driver)

