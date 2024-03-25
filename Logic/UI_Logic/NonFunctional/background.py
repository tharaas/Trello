from selenium.webdriver.common.by import By

from Infra.base_page import BasePage


class Background(BasePage):

    BACKGROUND = "//a[text()='Jason W']"

    def __init__(self, driver):
        super().__init__(driver)
        self.background = self._driver.find_element(By.XPATH, self.BACKGROUND)
        self.background_color = self.background.value_of_css_property("background-color")

    def change_background(self):
        self.background.click()

    def background_is_displayed(self):
        expected_color = "rgba(0, 0, 0, 0.5)"
        if self.background_color == expected_color:
            return True
        return False
