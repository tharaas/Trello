import time
import unittest

from Infra.api_wrapper import APIWrapper
from Infra.browser_wrapper import BrowserWrapper
from Logic.API_Logic.board_page_api import BoardPageAPI
from Logic.UI_Logic.Functional.home_page import HomePage
from Utils.login_logout import LoginPageActions
from jira_report import JiraReport


class NegativeTest(unittest.TestCase):
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
        self.driver.quit()
        if hasattr(self, '_outcome') and self._outcome.errors:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_create_board"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except AssertionError as e:
                print("Failed to report bug to Jira:", str(e))

    def test_search_board_that_does_not_exist(self):
        #search with API
        search_board_is_displayed = self.board_api.search_board_name_in_search_api("board_title")
        self.assertFalse(search_board_is_displayed, "The Board is not exit")
