import time
import unittest

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Logic.API_Logic.board_page_api import BoardPageAPI
from Logic.UI_Logic.Functional.board_page import BoardPage
from Logic.UI_Logic.Functional.create_board_button import CreateBoard
from Logic.UI_Logic.Functional.home_page import HomePage
from Utils.API_URL import UrlAPI
from Utils.login_logout import LoginPageActions
from jira_report import JiraReport


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.api_wrapper = APIWrapper()
        self.board_api = BoardPageAPI(self.api_wrapper)
        self.login = LoginPageActions(self.driver)
        self.login.fill_email_input_and_go_to_password_sign_in()
        time.sleep(2)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        #delete the board that the test create
        self.board_api.delete_board_from_api(self.title_id)
        self.driver.quit()
        if not self._outcome.success:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_create_board"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except AssertionError as e:
                print("Failed to report bug to Jira:", str(e))

    def test_create_board(self):
        #create board and add list in UI
        self.home_page.click_on_create_board_button()
        time.sleep(4)
        self.create_board = CreateBoard(self.driver)
        board_title = self.create_board.create_new_board()
        time.sleep(2)
        self.board_page = BoardPage(self.driver)
        self.board_page.add_list()
        self.url_id = UrlAPI()
        self.title_id = self.url_id.get_board_id(self.board_page.get_url_driver())
        board_name = self.board_api.get_board_from_api(self.title_id)
        self.assertEqual(board_name, board_title)