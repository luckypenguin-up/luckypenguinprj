from selenium.webdriver.common.by import By

from .base_page import BasePage
from .contact import Contact

class Main(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"
    def download(self):
        pass
    def import_user(self,file_path):
        self.find((By.LINK_TEXT,"导入通讯录")).click()
        self.find((By.LINK_TEXT, "填写通讯录模板后导入")).click()
        self.find((By.ID, "js_upload_file_input")).send_keys(file_path)
        self.find((By.ID, "submit_csv")).click()
        self.find((By.ID, "reloadContact")).click()
        return self
    def import_photo(self,file_path):
        self.find((By.LINK_TEXT,"管理工具")).click()
        self.find((By.CSS_SELECTOR,'.manageTools_cnt_item:nth-child(5) .manageTools_cnt_item_desc_title')).click()
        self.find((By.LINK_TEXT,"图片")).click()
        self.find((By.LINK_TEXT, "添加图片")).click()
        self.find((By.ID, "js_upload_input")).send_keys(file_path)
        self.find((By.LINK_TEXT, "完成")).click()
        return self
    def goto_app(self):
        pass
    def get_message(self):
        return ["aaa","bbbb"]
    def add_member(self):
        locator = (By.LINK_TEXT, '添加成员')
        #self.find(locator).click()
        self._driver.execute_script("arguments[0].click();",self.find(locator))#js点击，浏览器缩小比例后，点击不生效可以使用这个来实现点击
        return Contact(reuse=True)
