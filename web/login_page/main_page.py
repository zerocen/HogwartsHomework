import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from web.login_page.login_page import LoginPage
from web.login_page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

        # User cookie to log in
        with open("my_cookie", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def goto_contacts(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        return

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']").click()
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)
