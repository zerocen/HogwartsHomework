import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from web.contacts_page.contacts_page import ContactsPage


class UserHomePage:
    def __init__(self):
        # User cookie to log in
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("my_cookie", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        # Use remote debugging to login
        # chrome_arg = webdriver.ChromeOptions()
        # chrome_arg.debugger_address = '127.0.0.1:5000'
        # self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver.implicitly_wait(5)

    def goto_contacts(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        return ContactsPage(self.driver)
