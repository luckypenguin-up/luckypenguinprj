from selenium import webdriver
from selenium.webdriver.common.by import By


class hogwarzs:
    def setup_method(self):
        self.driver=webdriver.firefox
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)
    def test_hogwarz(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()


    def test_stsc2020(self):
        self.driver.get("")
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"").click()
        print(self.driver.window_handles)
        self.driver.switch_to.windows()