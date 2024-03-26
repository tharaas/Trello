from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage
from Utils.read_from_env_file_like_username_password import Credentials
from Utils.scroll import Scroll


class HomePage(BasePage):

    ACCOUNT_BUTTON = "//div[contains(@title,'Kakashi')]"
    BOARDS_BUTTON = "//span[text()='Boards' and contains(@class,'DD3DlImSMT6fgc XQSLFE3ZZrvms3')]"
    BOARD = "//div[text()='My Trello board']"
    CREATE_BOARD = "//span[text()='Create new board']"

    BOARD_TITLE = "//input[contains(@type,'text')]"
    CREATE_BUTTON = "//button[text()='Create']"

    def __init__(self, driver):
        super().__init__(driver)
        self.credentials = Credentials()
        self.scroll = Scroll(self._driver)
        self.account_button = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ACCOUNT_BUTTON)))
        self.board_button = self._driver.find_element(By.XPATH, self.BOARDS_BUTTON)
        self.board = self._driver.find_element(By.XPATH, self.BOARD)
        self.create_board = self._driver.find_element(By.XPATH, self.CREATE_BOARD)

        self.wait = WebDriverWait(driver, 10)

    def account_button_is_displayed(self):
        return self.account_button.is_displayed()

    def click_on_account_button(self):
        self.account_button.click()

    def click_on_board_button(self):
        self.board_button.click()

    def click_on_board(self):
        self.board.click()

    def click_on_create_board_button(self):
        self.create_board.click()
