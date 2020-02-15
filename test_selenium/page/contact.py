from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    _add_member_button=(By.CSS_SELECTOR,"xxx")
    def add_member(self,data):
        #self.driver.find_element("添加成员").click
        #send.keys
        #click save
        name_locator = (By.NAME,'username')
        acctid_locator = (By.NAME,'acctid')
        #gender_locator = (By.CSS_SELECTOR,'.ww_radio+span:contains("女")')#.ww_radio[value="2"]
        gender_locator = (By.CSS_SELECTOR,'.ww_radio[value="2"')
        mobile_locator = (By.NAME,'mobile')
        self.find(name_locator).send_keys("penguin")
        self.find(acctid_locator).send_keys("penguin")
        self.find(gender_locator).click()
        self.find(mobile_locator).send_keys("15600001234")
       # return self
    def search(self,name):
        pass
    def import_user(self,data):
        pass
    def set_department(self,data):
        pass
    def export_user(self,data):
        pass
    def delete(self):
        pass
    def invite(self):
        pass
