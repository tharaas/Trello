import time
import unittest

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Logic.API_Test.board_page_api import BoardPageAPI
from Logic.UI_Logic.Functional.create_board_button import CreateBoard
from Logic.UI_Logic.Functional.home_page import HomePage
from Utils.login import LoginPageActions


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.api_wrapper = APIWrapper()
        self.board_api = BoardPageAPI(self.api_wrapper)

        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = LoginPageActions(self.driver)
        self.login.fill_email_input_and_go_to_password_sign_in()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_board(self):
        self.home_page.click_on_create_board_button()
        time.sleep(4)
        self.create_board = CreateBoard(self.driver)
        self.create_board.create_new_board()

        board_data = self.board_api.get_board_from_api("random")
        print(board_data)
        #self.assertTrue(account_login, "Login was not successful")
