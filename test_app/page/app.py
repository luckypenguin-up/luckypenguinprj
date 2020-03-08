import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_app.page.base_page import BasePage
from test_app.page.main import Main
from selenium.webdriver.remote.webdriver import WebDriver

#app行为定义
class App(BasePage):
    #重新定义父类的driver
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    @property
    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "123"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            #caps["noReset"] = True  # 不重置数据
            # caps["dontStopAppOnReset"] = True#如果有进程，不杀进程
            # 设置键盘
            # caps["unicodeKeyboard"] = True
            # caps["resetKeyboard"] = True
            # caps["skipServerInstallation"] = True #提速
            caps["chromedriverExecutable"] = "/Users/liqian/Downloads/chromedriver-3"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:#不为空复用以前的driver
            print(self._driver)
            #todo:kill app start app
            self._driver.start_activity(self._package, self._activity)

        return self #链式调用的关键
    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:#类型提示，资料 python type hint  python.org/dev/peps/pep-0484/
        #todo:wait
        #WebDriverWait(self._driver,30).until(lambda x : "我的" in self._driver.page_source)
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            return False
        WebDriverWait(self._driver,30).until(wait_load)
        return Main(self._driver)

