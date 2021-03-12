import yaml
from appium import webdriver
from uifamework.page.base_page import BasePage
from uifamework.page.main_page import MainPage


with open("../data/config.yml") as f:
    data = yaml.safe_load(f)
    caps = data["caps"]
    command_executor = data["server"]["commandExecutor"]


class App(BasePage):

    def start(self):
        if self.driver is None:
            self.driver = webdriver.Remote(command_executor, caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main_page(self):
        return MainPage(self.driver)
