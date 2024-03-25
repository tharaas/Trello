import time

from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class BoardPage(BasePage):

    MENU_BUTTON = "//button[contains(@aria-label,'Show menu')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)

    def click_on_menu_button_in_board(self):
        self.menu_button.click()