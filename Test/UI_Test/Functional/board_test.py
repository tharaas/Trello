import time
import unittest

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Logic.API_Logic.board_page_api import BoardPageAPI
from Logic.UI_Logic.Functional.board_menu import BoardMenu
from Logic.UI_Logic.Functional.board_page import BoardPage
from Logic.UI_Logic.Functional.create_board_button import CreateBoard
from Logic.UI_Logic.Functional.home_page import HomePage
from Utils.login_logout import LoginPageActions


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.api_wrapper = APIWrapper()
        self.board_api = BoardPageAPI(self.api_wrapper)

        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = LoginPageActions(self.driver)
        self.login.fill_email_input_and_go_to_password_sign_in()
        time.sleep(2)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.board_page.click_on_menu_button_in_board()
        self.board_menu = BoardMenu(self.driver)
        self.board_menu.delete_board()
        self.driver.quit()

    def test_create_board(self):
        self.home_page.click_on_create_board_button()
        time.sleep(4)
        self.create_board = CreateBoard(self.driver)
        self.create_board.create_new_board()
        time.sleep(2)
        self.board_page = BoardPage(self.driver)
        self.board_page.add_list()
        self.board_page.add_card()
        #self.board_menu.close_boutton()
        #board_data = self.board_api.get_board_from_api("random")
        #self.assertTrue(account_login, "Login was not successful")


