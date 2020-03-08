from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import  logging

class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver  # 存放driver的对象 改造成android driver
    _black_list=[
        (By.ID,'image_cancel'),
        (By.ID, 'tv_agree'),
        (By.XPATH,'//*[@text="确定"]'),
        (By.XPATH,'//*[@text="下次再说"]')
    ]
    _error_max = 10
    def __init__(self, driver: WebDriver = None):  # 接受app的driver方法
        self._driver = driver
    #todo: 当有广告。评价各种弹窗，要进行异常流程处理
    #视频讲解在15章第一节：10分钟
    def find(self,locator,value:str = None):
        logging.info(locator)
        logging.info(value)
        try:
            #寻找控件
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            #如成功，清空历史错误次数
            self._error_max = 0
            return element
            # if isinstance(locator, tuple):#如果是元组
            #     return self._driver.find_element(*locator)
            # else:
            #     return self._driver.find_element(locator, value)
          #done:  self._error_max = 0
        except Exception as e:
            #如果次数太多，退出异常
            if self._error_max > 10:
                raise e #抛出异常
            else:
                self._error_max+=1
                #对黑名单进行处理
                for element in self._black_list:
                    logging.info(element)
                    elements = self._driver.find_elements(*element)#元素找不到 也不会抛出异常
                    if len(elements) > 0:
                        elements[0].click()
                #继续寻找正常控件
                return self.find(locator,value)#啥含义


    def get_toast(self):
        return  self.find(By.XPATH,"//*[@class='android.widget.Toast']").text

    def text(self,key):#定位符中使用变量
        return (By.XPATH,"//*[@text='%s']" % key)

    def find_by_text(self,key):
        return self.find(self.text(key))