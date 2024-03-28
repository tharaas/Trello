import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage
from Utils.random_text import RandomText


class BoardPage(BasePage):

    MENU_BUTTON = "//button[contains(@aria-label,'Show menu')]"
    LIST_TITLE = "//textarea[contains(@name,'Enter')]"
    ADD_TO_LIST = "//button[text()='Add list']"
    ADD_A_CARD = "//button[text()='Add a card']"
    ADD_TITLE_FOR_THE_CARD = "//textarea[contains(@placeholder,'title for this card')]"
    ADD_CARD_BUTOON = "//button[text()='Add card']"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.random_text = RandomText(self._driver)
        self.menu_button = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.MENU_BUTTON)))

    def click_on_menu_button_in_board(self):
        self.menu_button.click()

    def get_list_title(self):
        self.list_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.LIST_TITLE)))
        title_board = self.random_text.get_random_title()
        self.list_title.send_keys(title_board)
        return title_board

    def clcik_on_add_to_list(self):
        self.add_to_list_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ADD_TO_LIST)))
        self.add_to_list_button.click()

    def add_list(self):
        title_list = self.get_list_title()
        self.clcik_on_add_to_list()
        return title_list

    def add_card_to_the_list(self):
        self.add_a_card_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ADD_A_CARD)))
        self.add_a_card_button.click()

    def add_title_for_the_card(self):
        self.add_title_card = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ADD_TITLE_FOR_THE_CARD)))
        self.add_title_card.send_keys(self.random_text.get_random_title())

    def add_card_to_the_list_with_title(self):
        self.card_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ADD_TITLE_FOR_THE_CARD)))
        self.card_button.click()

    def add_card(self):
        self.add_card_to_the_list()
        time.sleep(2)
        self.add_title_for_the_card()
        self.add_card_to_the_list_with_title()
