from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class AccountMenu(BasePage):

    PROFILE_BUTTON = "//span[text()='Profile and visibility']"
    SETTING_BUTTON = "//span[text()='Settings']"
    THEME_BUTTON = "//span[text()='Theme']"

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_button = self._driver.find_element(By.XPATH, self.PROFILE_BUTTON)
        self.setting_button = self._driver.find_element(By.XPATH, self.SETTING_BUTTON)
        self.theme_button = self._driver.find_element(By.XPATH, self.THEME_BUTTON)

    def click_on_profile_button(self):
        self.profile_button.click()

    def click_on_setting_button(self):
        self.setting_button.click()

    def click_on_theme_button(self):
        self.theme_button.click()
