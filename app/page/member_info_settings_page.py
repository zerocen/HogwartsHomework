from app.page.base_page import BasePage
from app.page.edit_member_info_page import EditMemberInfoPage


class MemberInfoSettingsPage(BasePage):

    def goto_edit_member_info_page(self):
        return EditMemberInfoPage(self.driver)
