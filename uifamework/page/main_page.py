from appium.webdriver.common.mobileby import MobileBy
from uifamework.page.base_page import BasePage
from uifamework.page.market_page import MarketPage


class MainPage(BasePage):

    def goto_market_page(self):
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(MobileBy.XPATH, "//*[@text='行情']")
        self.perform_function("../data/main_page.yml", "goto_market")
        return MarketPage(self.driver)

    def goto_market_page_2(self):
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.finds(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']/android.widget.RelativeLayout")[1].click()
        return MarketPage(self.driver)
