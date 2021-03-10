from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from app.page.add_member_page import AddMemberPage
from app.page.base_page import BasePage
from app.page.member_info_page import MemberInfoPage


class ContactsPage(BasePage):

    def goto_add_member_page(self):
        # self.swipe_find("添加成员").click()
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)

    def goto_member_info_page_by_search(self, name):
        self.find_and_click(MobileBy.XPATH,
                            "(//*[@text='Zerolab']/ancestor::android.widget.RelativeLayout[1]//android.widget.TextView)[2]")
        self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        self.finds(MobileBy.XPATH, f"//*[contains(@text, '联系人')]/../..//*[starts-with(@text, '{name}')]").click()
        return MemberInfoPage(self.driver)
