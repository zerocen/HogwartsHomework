from uiframework.page.base_page import BasePage
from uiframework.page.search_page import SearchPage


class MarketPage(BasePage):

    def goto_search_page(self):
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.perform_function("../data/market_page.yml", "goto_search")
        return SearchPage(self.driver)
