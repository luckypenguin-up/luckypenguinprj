from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page import register
from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()
        # self.driver = webdriver.Chrome()  # 设置浏览器
        # self.driver.implicitly_wait(3)  # 设置隐式等待
        # self.driver.get("https://work.weixin.qq.com/")

    def test_register(self):
        # index = Index(self.driver)
        self.index.goto_register().register("testlixi")
        # self.driver.find_element(By.LINK_TEST,"立即注册").click()
        # self.driver.find_element(By.ID,"corp_name").send_keys("testlixi")
        # self.driver.find_element(By.ID,"submit_btn").click()

    def test_login(self):
        register_page = self.index.goto_login().goto_registry().register("测试吧")
        print(register_page.get_error_message())
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
