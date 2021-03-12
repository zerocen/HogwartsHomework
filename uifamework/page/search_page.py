from appium.webdriver.common.mobileby import MobileBy
from uifamework.page.base_page import BasePage


class SearchPage(BasePage):

    def search(self, key_word):
        self.find_and_send_keys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", key_word)
