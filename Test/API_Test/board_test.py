import time
import unittest

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Logic.API_Logic.board_page_api import BoardPageAPI
from Logic.UI_Logic.Functional.board_menu import BoardMenu
from Logic.UI_Logic.Functional.board_page import BoardPage
from Logic.UI_Logic.Functional.create_board_button import CreateBoard
from Logic.UI_Logic.Functional.home_page import HomePage
from Utils.API_URL import UrlAPI
from Utils.login_logout import LoginPageActions


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()

        #self.api_wrapper = APIWrapper()
        #self.board_api = BoardPageAPI(self.api_wrapper)
        self.login = LoginPageActions(self.driver)
        self.login.fill_email_input_and_go_to_password_sign_in()
        time.sleep(2)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_board(self):
        self.home_page.click_on_create_board_button()
        time.sleep(4)
        self.create_board = CreateBoard(self.driver)
        board_title = self.create_board.create_new_board()
        time.sleep(2)
        self.board_page = BoardPage(self.driver)
        self.board_page.add_list()
        #self.board_page.add_card()
        #self.url_id = UrlAPI()
        #id = self.url_id.get_board_id(self.driver.get_url_driver())
        #board_name = self.board_api.get_board_from_api(id)
        #print(board_name)
        #self.assertEqual(board_name, board_title)
