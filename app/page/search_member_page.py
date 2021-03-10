from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage
from app.page.member_info_page import MemberInfoPage


class SearchMemberPage(BasePage):

    def search_and_goto_member_info_page(self, name):

        self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        results = self.finds(MobileBy.XPATH, f"//*[contains(@text, '联系人')]/../..//*[starts-with(@text, '{name}')]")
        if len(results) > 0:
            results[0].click()
        else:
            raise Exception(f"The member {name} doesn't exist.")

        return MemberInfoPage(self.driver)

    def verify_member_not_exist(self, name):
        results = self.finds(MobileBy.XPATH, f"//*[contains(@text, '联系人')]/../..//*[starts-with(@text, '{name}')]")
        return len(results) == 0
