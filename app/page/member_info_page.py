from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage
from app.page.member_info_settings_page import MemberInfoSettingsPage


class MemberInfoPage(BasePage):

    def goto_member_info_settings_page(self):
        self.find_and_click(MobileBy.XPATH, "(//*[@text='个人信息']/ancestor::android.widget.RelativeLayout[1]"
                                            "//android.widget.TextView)[last()]")
        return MemberInfoSettingsPage(self.driver)
