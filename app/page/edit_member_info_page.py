from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class EditMemberInfoPage(BasePage):

    def delete_member(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")