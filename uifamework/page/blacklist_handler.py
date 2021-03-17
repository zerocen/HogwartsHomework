from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def handle_blacklist(func):

    def wrapper(*args, **kwargs):
        blacklist = ["//*[@resource-id='com.xueqiu.android:id/iv_close']",
                     "//*[@resource-id='com.xueqiu.android:id/tv_agree']",
                     "//*[@resource-id='com.xueqiu.android:id/tv_skip']"]
        instance = args[0]
        try:
            obj = func(*args, **kwargs)
            if isinstance(obj, list) and len(obj) == 0:
                raise NoSuchElementException("Failed to find elements.")
            return obj
        except (StaleElementReferenceException, NoSuchElementException):
            for xpath in blacklist:
                elements = instance.driver.find_elements(MobileBy.XPATH, xpath)
                if len(elements) > 0:
                    elements[0].click()
                    return func(*args, **kwargs)

    return wrapper
