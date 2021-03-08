from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, selector, value):
        return self.driver.find_element(selector, value)

    def finds(self, selector, value):
        return self.driver.find_elements(selector, value)

    def find_and_click(self, selector, value):
        self.find(selector, value).click()

    def swipe_find(self, xpath, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"滑动寻找{num}次，未找到元素")

            self.driver.implicitly_wait(1)

            try:
                element = self.driver.find_element(MobileBy.XPATH, xpath)
                self.driver.implicitly_wait(5)
                return element
            except NoSuchElementException:
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
