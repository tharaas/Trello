
from selenium.webdriver.common.by import By

from Infra.base_page import BasePage


class ChangeBackground(BasePage):

    CHANGE_BACKGROUND = "//div[text()='Photos']"

    def __init__(self, driver):
        super().__init__(driver)
        self.change_background = self._driver.find_element(By.XPATH, self.CHANGE_BACKGROUND)

    def click_on_change_background_button(self):
        self.change_background.click()

