from appium.webdriver.common.mobileby import MobileBy
from app.page.add_member_page import AddMemberPage
from app.page.base_page import BasePage
from app.page.member_info_page import MemberInfoPage


class ContactsPage(BasePage):

    def goto_add_member_page(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)

    def goto_member_info_page_by_search(self):
        return MemberInfoPage(self.driver)
