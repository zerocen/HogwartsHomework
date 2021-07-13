from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find(locator).click()
        # element = self.find(locator)
        # try:
        #     element.click()
        # except ElementClickInterceptedException:
        #     self.driver.execute_script("arguments[0].click();", element)
        # except ElementNotInteractableException:
        #     self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        #     WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator)).click()
