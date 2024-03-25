from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class TrelloPage(BasePage):

    LOGIN_BUTTON = "//header[contains(@class,'BigNavstyles__Header')]//a[text()='Log in']"
    SIGNUP_BUTTON = "//div[contains(@class,'eXMZwc')]//button[text()='Sign up - it’s free!']"

    def __init__(self, driver):
        super().__init__(driver)
        self.login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        self.signup_button = self._driver.find_element(By.XPATH, self.SIGNUP_BUTTON)

    def click_on_log_in_button(self):
        self.login_button.click()

