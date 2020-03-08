from selenium.webdriver.common.by import By

from test_app.page.base_page import BasePage


class Profile(BasePage):

    def login(self,phone,passwd):
        self.find(By.XPATH, '//*[@text="帐号密码登录"]').click()
        self.find(By.ID, "login_account").send_keys(phone)
        self.find(By.ID, "login_password").send_keys(passwd)
        self.find(By.ID, "button_next").click()
        msg = self.find(By.ID, "md_content").text
        self.find(By.ID,"md_buttonDefaultPositive").click()
        self.find(By.XPATH,"//*[@class='android.widget.Toast']").text#弹窗定位
        return msg
