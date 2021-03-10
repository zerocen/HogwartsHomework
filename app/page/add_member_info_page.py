from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage


class AddMemberInfoPage(BasePage):

    def add_member_simplify(self, name, mobile_phone):
        self.driver.implicitly_wait(1)
        found_elements = self.finds(MobileBy.XPATH, "//*[@text='快速输入']")
        if (len(found_elements)) > 0:
            found_elements[0].click()
        self.driver.implicitly_wait(5)

        # 姓名
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']") \
            .send_keys(name)
        # 手机
        self.find(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']") \
            .send_keys(mobile_phone)

        self.find(MobileBy.XPATH, "//*[contains(@text, '保存')]").click()
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")

    def add_member_completely(self, name, account, alias, gender, mobile_phone, telephone, email, address,
                              position, department, role):

        self.driver.implicitly_wait(1)
        found_elements = self.finds(MobileBy.XPATH, "//*[@text='完整输入']")
        if (len(found_elements)) > 0:
            found_elements[0].click()
        self.driver.implicitly_wait(5)

        # 姓名
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText") \
            .send_keys(name)
        # 帐号
        self.find(MobileBy.XPATH, "//*[contains(@text, '帐号')]/../android.widget.EditText") \
            .send_keys(account)
        # 别名
        self.find(MobileBy.XPATH, "//*[contains(@text, '别名')]/../android.widget.EditText") \
            .send_keys(alias)
        # 手机
        self.find(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//android.widget.EditText") \
            .send_keys(mobile_phone)
        # 座机
        self.find(MobileBy.XPATH, "//*[contains(@text, '座机')]/../android.widget.EditText") \
            .send_keys(telephone)
        # 邮箱
        self.find(MobileBy.XPATH, "//*[contains(@text, '邮箱')]/../android.widget.EditText") \
            .send_keys(email)
        # 职务
        self.find(MobileBy.XPATH, "//*[contains(@text, '职务')]/../android.widget.EditText") \
            .send_keys(position)

        # 设置性别
        self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/../android.widget.RelativeLayout").click()
        self.find(MobileBy.XPATH, f"//*[@text='{gender}']").click()

        # 填写地址
        self.find(MobileBy.XPATH, "//*[contains(@text, '地址')]/../android.widget.RelativeLayout").click()
        self.find(MobileBy.XPATH, "//*[contains(@text, '请输入')]").send_keys(address)
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()

        # 设置部门
        self.find(MobileBy.XPATH, "//*[@text='设置部门']").click()
        self.find(MobileBy.XPATH, f"//*[@text='{department}']").click()
        self.find(MobileBy.XPATH, "//*[contains(@text, '确定')]").click()

        # 设置身份
        self.find(MobileBy.XPATH, "//*[@text='身份']/../android.widget.RelativeLayout").click()
        self.find(MobileBy.XPATH, f"//*[@text='{role}']").click()

        self.swipe_find("保存").click()

        # self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
        #                                                        '.scrollable(true).instance(0))'
        #                                                        '.scrollIntoView(new UiSelector()'
        #                                                        '.text("保存").instance(0));').click()

        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
