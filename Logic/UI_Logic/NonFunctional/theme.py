from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage


class Theme(BasePage):

    DARK_BUTTON = "//div[text()='Dark']"
    DARK_MODE = "//button[contains(@class,'ez93Vb6EkWGC4q')]//div[text()='Dark']"
    LIGHT_BUTTON = "//div[text()='Light']"
    LIGHT_MODE = "//button[contains(@class,'ez93Vb6EkWGC4q')]//div[text()='Light']"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.dark_button = self._driver.find_element(By.XPATH, self.DARK_BUTTON)
        self.light_button = self._driver.find_element(By.XPATH, self.LIGHT_BUTTON)

    def click_on_dark_button(self):
        self.dark_button.click()
        return self.dark_mode_is_displayed()

    def dark_mode_is_displayed(self):
        try:
            self.dark_mode = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.DARK_MODE)))
            return True
        except TimeoutException:
            return False

    def click_on_light_button(self):
        self.light_button.click()
        return self.light_mode_is_displayed()

    def light_mode_is_displayed(self):
        try:
            self.light_mode = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.LIGHT_MODE)))
            return True
        except TimeoutException:
            return False
