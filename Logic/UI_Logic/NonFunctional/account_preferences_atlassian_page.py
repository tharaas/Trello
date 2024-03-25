from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class AtlassianAccountPage(BasePage):

    Language = "//div[text()='English (US)']"

    def __init__(self, driver):
        super().__init__(driver)
        self.language = self._driver.find_element(By.XPATH, self.Language)

    def click_on_language(self):
        self.language.click()


