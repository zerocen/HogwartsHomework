from appium import webdriver
from app.page.base_page import BasePage
from app.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "98221FFAZ000EJ",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "skipDeviceInitialization": True,
                "skipServerInstallation": True,
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
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
