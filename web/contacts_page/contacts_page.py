from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_member(self, name, account, phone):

        def wait_form(driver):
            try:
                # 此处获取的元素可能无效，需要重复获取直到有效
                driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
                driver.find_element(By.XPATH, "//*[@id='username']").click()
            except StaleElementReferenceException:
                return False

            return True

        WebDriverWait(self.driver, 10).until(wait_form)

        # Input name, account id, phone
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(name)
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys(account)
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys(phone)

        # Save
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
