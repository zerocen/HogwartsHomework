from appium.webdriver.common.mobileby import MobileBy
from app.page.add_member_info_page import AddMemberInfoPage
from app.page.base_page import BasePage


class AddMemberPage(BasePage):

    def goto_add_member_info_page(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return AddMemberInfoPage(self.driver)
