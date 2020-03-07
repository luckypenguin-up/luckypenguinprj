from appium import webdriver

from test_app.page.main import Main

#app行为定义
class App:
    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "123"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True  # 不重置数据
        # caps["dontStopAppOnReset"] = True#如果有进程，不杀进程
        # 设置键盘
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True #提速
        caps["chromedriverExecutable"] = "/Users/liqian/Downloads/chromedriver-3"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

        return self #链式调用的关键

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:#类型提示，资料 python type hint  python.org/dev/peps/pep-0484/
        #todo:wait
        return Main(self.driver)

