from appium.webdriver.common.mobileby import MobileBy
from app.page.add_member_page import AddMemberPage
from app.page.base_page import BasePage
from app.page.search_member_page import SearchMemberPage


class ContactsPage(BasePage):

    def goto_add_member_page(self):
        # self.swipe_find("添加成员").click()
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)

    def goto_search_member_page(self):
        self.find_and_click(MobileBy.XPATH, "(//*[@text='Zerolab']/ancestor::android.widget.RelativeLayout[1]"
                                            "//android.widget.TextView)[2]")
        return SearchMemberPage(self.driver)
