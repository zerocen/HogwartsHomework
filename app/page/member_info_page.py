from app.page.base_page import BasePage
from app.page.member_info_settings_page import MemberInfoSettingsPage


class MemberInfoPage(BasePage):

    def goto_member_info_settings_page(self):
        return MemberInfoSettingsPage(self.driver)