import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class BasePage:

    logging.basicConfig(level=logging.INFO, filename="../logs/test_log.log",
                        format="[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]", filemode="a",
                        datefmt="'%Y-%m-%d %I:%M:%S %p'")

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def handle_blacklist(func):
        blacklist = ["//*[@resource-id='com.xueqiu.android:id/iv_close']",
                     "//*[@resource-id='com.xueqiu.android:id/tv_agree']",
                     "//*[@resource-id='com.xueqiu.android:id/tv_skip']"]

        def wrapper(self, *args, **kwargs):
            try:
                obj = func(self, *args, **kwargs)
                if isinstance(obj, list) and len(obj) == 0:
                    raise NoSuchElementException("Failed to find elements.")
                return obj
            except (StaleElementReferenceException, NoSuchElementException):
                for xpath in blacklist:
                    elements = self.driver.find_elements(MobileBy.XPATH, xpath)
                    if len(elements) > 0:
                        elements[0].click()
                        return func(self, *args, **kwargs)
                # else:
                    # Some elements in the black list may disappear automatically, such as ad. Find the target again.
                    # return wrapper(self, *args, **kwargs)

        return wrapper

    @handle_blacklist
    def find(self, locator, value):
        logging.info(f"find element: {(locator, value)}")
        return self.driver.find_element(locator, value)

    @handle_blacklist
    def finds(self, locator, value):
        logging.info(f"find elements: {(locator, value)}")
        return self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):
        element = self.find(locator, value)
        logging.info(f"click element: {(locator, value)}")
        element.click()

    def find_and_send_keys(self, locator, value, key_value):
        self.find(locator, value).send_keys(key_value)

    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"滑动寻找{num}次，未找到元素")

            self.driver.implicitly_wait(1)

            try:
                element = self.find(MobileBy.XPATH, f"//*[@text={text}]")
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
