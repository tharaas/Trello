import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage
from Utils.read_from_env_file_like_username_password import Credentials


class LogInPage(BasePage):

    LOGIN_PAGE = "//h5[text()='Log in to continue']"
    EMAIL_INPUT = "//input[@type='email']"
    CONTINUE_BUTTON = "//span[text()='Continue']"
    PASSWORD_INPUT = "//input[@type='password']"
    SIGN_IN_BUTTON = "//span[text()='Log in']"

    def __init__(self, driver):
        super().__init__(driver)
        self.credentials = Credentials()
        self.login_page = self._driver.find_element(By.XPATH, self.LOGIN_PAGE)
        self.email_button = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self.continue_button = self._driver.find_element(By.XPATH, self.CONTINUE_BUTTON)
        self.password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)

        self.wait = WebDriverWait(driver, 10)
        self.SIGN_IN_BUTTON = (By.XPATH, self.SIGN_IN_BUTTON)

    def login_button_is_displayed(self):
        return self.login_page.is_displayed()

    def fill_email_input_login(self):
        email = self.credentials.get_email()
        self.email_button.send_keys(email)

    def click_continue_fill_email_input_login(self):
        self.continue_button.click()

    def fill_password_input_login(self):
        password = self.credentials.get_password()
        self.password_input.send_keys(password)

    def click_login_fill_email_and_password_input(self):
        self.continue_button.click()

    def fill_email_input_and_go_to_password_sign_in_with_google(self):
        self.fill_email_input_login()
        self.click_continue_fill_email_input_login()
        time.sleep(5)
        self.fill_password_input_login()
        self.click_login_fill_email_and_password_input()
