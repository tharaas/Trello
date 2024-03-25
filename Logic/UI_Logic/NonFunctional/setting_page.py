from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class SettingPage(BasePage):

    Language_BUTTON = "//span[text()='Change language']"

    def __init__(self, driver):
        super().__init__(driver)
        self.language_button = self._driver.find_element(By.XPATH, self.Language_BUTTON)

    def click_on_language_button(self):
        self.language_button.click()


