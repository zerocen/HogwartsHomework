from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage
from app.page.edit_member_info_page import EditMemberInfoPage


class MemberInfoSettingsPage(BasePage):

    def goto_edit_member_info_page(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return EditMemberInfoPage(self.driver)
