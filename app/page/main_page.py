from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage
from app.page.contacts_page import ContactsPage


class MainPage(BasePage):

    def goto_contacts_page(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactsPage(self.driver)
