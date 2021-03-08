import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestWeCom:

    def setup_class(self):
        caps = {
            "platformName": "android",
            "platformVersion": "10",
            "deviceName": "98221FFAZ000EJ",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "automationName": "UiAutomator2",
            "skipDeviceInitialization": True,
            "skipServerInstallation": True,
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "settings[waitForIdleTimeout]": 3
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()

    def teardown_class(self):
        self.driver.quit()

    def swipe_find(self, xpath, num=3):

        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"滑动寻找{num}次，未找到元素")
            try:
                element = self.driver.find_element(MobileBy.XPATH, xpath)
                return element
            except NoSuchElementException:
                size = self.driver.get_window_size()
                width = size.get()
                height = size.get()
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    @pytest.mark.parametrize("name, account, alias, gender, mobile_phone, telephone, email, address, position, "
                             "department, role", [
                                 ("张三", "ZhangSan", "zs", "男", "12345678900", "021456789", "zhangsan@test.com",
                                  "XXX路XX号", "总经理", "市场部", "上级"),
                                 ("Keely", "keely", "k", "女", "18545654585", "021001155", "keely@test.com",
                                  "XXX路1号", "工程师", "技术部", "普通成员"),
                                 ("Erwin", "erwin", "e", "男", "15677895422", "021021554", "erwin@test.com",
                                  "XXX路2号", "产品经理", "产品部", "普通成员")
                             ])
    def test_add_member(self, name, account, alias, gender, mobile_phone, telephone, email, address, position,
                        department, role):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        edits = self.driver.find_elements(MobileBy.XPATH, "//android.widget.EditText")
        # 姓名
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText") \
            .send_keys(name)
        # 账号
        edits[1].send_keys(account)
        # 别名
        edits[2].send_keys(alias)
        # 手机
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//android.widget.EditText") \
            .send_keys(mobile_phone)

        edits[3].send_keys(mobile_phone)
        # 座机
        edits[4].send_keys(telephone)
        # 邮箱
        edits[5].send_keys(email)
        # 职位
        edits[6].send_keys(position)

        # 设置性别
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.ScrollView//android.widget.RelativeLayout[4]").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{gender}']").click()

        # 填写地址
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.ScrollView//android.widget.RelativeLayout[8]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '请输入')]").send_keys(address)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        # 设置部门
        self.driver.find_element(MobileBy.XPATH, "//*[@text='设置部门']").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{department}']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '确定')]").click()

        # 设置身份
        if role == '上级':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='普通成员']").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='上级']").click()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                               '.scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector()'
                                                               '.text("保存").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
