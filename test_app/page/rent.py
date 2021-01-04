from appium.webdriver.common.mobileby import MobileBy
from djcelery.admin_utils import action
from selenium.webdriver.common.by import By

from test_app.page.base_page import BasePage


class Rent(BasePage):
    def search(self, key):
        self.find(By.XPATH, "//*[contains(@class,'androidx.appcompat.widget.LinearLayoutCompat')]").click()
        self.find(MobileBy.ID, "ocet_edit").send_keys(key)
        self._driver.execute_script("mobile:performEditorAction", {"action": "search"})

    def book(self):
        self.find(MobileBy.ID, "tv_click_box_book").click()
        self.find(By.XPATH, "//*[contains(@resource-id,'box_book_level_list')]/android.view.ViewGroup[1]").click()