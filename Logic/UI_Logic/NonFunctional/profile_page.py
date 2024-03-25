from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage
from Utils.random_text import RandomText
from Utils.read_from_env_file_like_username_password import Credentials
from Utils.scroll import Scroll


class ProfilePage(BasePage):

    BIO_TEXT = "//textarea[@id='bio']"
    SAVE_BUTTON = "//button[text()='Save']"

    def __init__(self, driver):
        super().__init__(driver)
        self.credentials = Credentials()
        self.scroll = Scroll(self._driver)
        self.random_text = RandomText(self._driver)
        self.new_bio_text = self.random_text.get_random_sentence()
        self.bio_text = self._driver.find_element(By.XPATH, self.BIO_TEXT)

        self.wait = WebDriverWait(driver, 10)
        self.save_button = (By.XPATH, self.SAVE_BUTTON)

    def click_on_bio_text(self):
        self.bio_text.click()

    def change_bio_text(self):
        self.click_on_bio_text()
        self.bio_text.clear()
        self.bio_text.send_keys(self.new_bio_text)

    def save_change(self):
        self.scroll.scrollHeight()
        self.save = self.wait.until(EC.element_to_be_clickable(self.save_button))
        self.save.click()

    def change_bio_flow(self):
        self.click_on_bio_text()
        self.change_bio_text()
        self.scroll.scrollHeight()
        self.save_change()

    def get_bio_text(self):
        return self.bio_text.get_attribute("value")

    def save_changes_is_displayed(self):
        if self.new_bio_text == self.get_bio_text():
            return True
        return False
