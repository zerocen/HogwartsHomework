from appium.webdriver.common.mobileby import MobileBy
from uifamework.page.base_page import BasePage
from uifamework.page.search_page import SearchPage


class MarketPage(BasePage):

    def goto_search_page(self):
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        return SearchPage(self.driver)