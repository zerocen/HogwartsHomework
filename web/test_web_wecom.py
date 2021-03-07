import json
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from web.contacts_page.user_home_page import UserHomePage
from web.login_page.main_page import MainPage


class TestWorkWeixin:

    # Homework 1
    def test_login_by_remote_debugging(self):
        # User is logged in at the moment
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:5000'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_index']").click()

        # Get user cookie
        with open("my_cookie", "w", encoding="utf-8") as f:
            cookies = self.driver.get_cookies()
            json.dump(cookies, f)
        sleep(1)

    # Homework 1
    def test_login_by_cookie(self):
        self.driver = webdriver.Chrome()

        # Go to user homepage
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # Read cookie file
        with open("my_cookie", "r", encoding="utf-8") as f:
            cookies = json.load(f)

        # Add cookies
        for cookie in cookies:
            print(cookie)
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(3)
        self.driver.quit()

    # Homework 2
    @pytest.mark.parametrize("name, account, phone", [("Richard", "richard", "17822246213"),
                                                      ("Joanna", "joanna", "15678982254"),
                                                      ("Harris", "harris", "13658542221")
                                                      ])
    def test_add_member(self, name, account, phone):
        home_page = UserHomePage()
        home_page.goto_contacts().add_member(name, account, phone)

    def test_register(self):
        MainPage().goto_register().register()
        sleep(3)

    def test_login_register(self):
        MainPage().goto_login().goto_register().register()
        sleep(3)
