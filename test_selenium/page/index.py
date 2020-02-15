from selenium.webdriver.common.by import By

from .Login import Login
from .base_page import BasePage
from .register import Register


class Index(BasePage):
        _base_url="https://work.weixin.qq.com/"

        def goto_register(self):
           # self._driver.find_element(By.LINK_TEXT, "立即注册").click()
            self.find((By.LINK_TEXT, "立即注册")).click()
            return Register(self.find)
        def goto_login(self):
            #self._driver.find_element(By.LINK_TEXT, "企业登录").click()
            self.find((By.LINK_TEXT, "企业登录")).click()
            return Login(self.find)