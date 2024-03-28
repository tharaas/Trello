import time

from selenium.webdriver.common.by import By

from Infra.base_page import BasePage


class Background(BasePage):

    BACKGROUND = "//span[contains(@data-testid,'board-background-select-photo-9')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.background = self._driver.find_element(By.XPATH, self.BACKGROUND)
        self.background_color = self.background.value_of_css_property("background-color")

    def change_background(self):
        self.background.click()
        time.sleep(6)

    def background_is_displayed(self):
        expected_color = "rgba(0, 0, 0, 0.5)"
        if self.background_color == expected_color:
            return False
        return True
