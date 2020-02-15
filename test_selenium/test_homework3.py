from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class Testhomework3():
    def setup_method(self):
        chromeOptions = Options()
        chromeOptions.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/Users/liqian/tmp/selenium"
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")#复用浏览器
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.implicitly_wait(5)  # 隐式

    def teardown_method(self):
        self.driver.quit()

    def test_homework3(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, 'menu_contacts').click()
        WebDriverWait(self.driver, 10).until(self.wait_element)#显式等待，指定元素
        # sleep(10)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_bi_clickable((By.CSS_SELECTOR,'.js_has_member div:nth-child(1) .js_add_member')))
        self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        self.driver.find_element(By.ID, 'username').send_keys('test1')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('test11')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('13411112222')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def wait_element(self, x):
        size: int = len(self.driver.find_elements(By.ID, 'username'))
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1
