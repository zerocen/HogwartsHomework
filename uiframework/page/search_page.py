from uiframework.page.base_page import BasePage


class SearchPage(BasePage):

    def search(self):
        # self.find_and_send_keys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", key_word)
        self.perform_function("../data/search_page.yml", "search")
