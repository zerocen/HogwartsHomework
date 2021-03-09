from appium.webdriver.common.mobileby import MobileBy
from app.page.add_member_page import AddMemberPage
from app.page.base_page import BasePage
from app.page.member_info_page import MemberInfoPage


class ContactsPage(BasePage):

    def goto_add_member_page(self):
        self.swipe_find("添加成员").click()
        # self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)

    def goto_member_info_page_by_search(self, name):
        self.find_and_click(MobileBy.XPATH,
                            "//*[@text='Zerolab']/ancestor::android.widget.RelativeLayout[1]//android.widget.TextView")
        self.find(MobileBy.XPATH, "//*[@text='搜索']").send_keys("11")

        # 显示等待知道搜出两个元素 todo
        elements = self.finds(MobileBy.XPATH, f"//*[@text='{name}']")
        if len(elements) > 1:
            elements[1].click()
        return MemberInfoPage(self.driver)
