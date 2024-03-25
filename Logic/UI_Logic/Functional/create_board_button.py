from selenium.webdriver.common.by import By
from Infra.base_page import BasePage
from Utils.random_text import RandomText
from Utils.read_from_env_file_like_username_password import Credentials


class CreateBoard(BasePage):
    BOARD_TITLE = "//input[contains(@type,'text')]"
    CREATE_BUTTON = "//button[text()='Create']"

    def __init__(self, driver):
        super().__init__(driver)
        self.credentials = Credentials()
        self.board_title_element = self._driver.find_element(By.XPATH, self.BOARD_TITLE)
        self.create_button_element = self._driver.find_element(By.XPATH, self.CREATE_BUTTON)
        self.random_text = RandomText(self._driver)

    def click_on_board_title_button(self):
        self.board_title_element.click()

    def title_for_board(self):
        self.board_title_element.send_keys(self.random_text.get_random_title())

    def get_title(self):
        self.click_on_board_title_button()
        self.title_for_board()

    def click_create_button(self):
        self.create_button_element.click()

    def create_new_board(self):
        self.get_title()
        self.click_create_button()
