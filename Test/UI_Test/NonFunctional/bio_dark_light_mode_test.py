import unittest
import time

from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_Logic.Functional.account_menu import AccountMenu
from Logic.UI_Logic.Functional.home_page import HomePage
from Logic.UI_Logic.NonFunctional.profile_page import ProfilePage
from Logic.UI_Logic.NonFunctional.theme import Theme
from Utils.login_logout import LoginPageActions
from jira_report import JiraReport


class NonFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = LoginPageActions(self.driver)
        self.login.fill_email_input_and_go_to_password_sign_in()

        self.home_page = HomePage(self.driver)
        self.home_page.click_on_account_button()
        time.sleep(2)
        self.account = AccountMenu(self.driver)

    def tearDown(self):
        self.driver.quit()
        if hasattr(self, '_outcome') and self._outcome.errors:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_board_change_background"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_change_bio_from_profile_page(self):
        self.account.click_on_profile_button()
        time.sleep(2)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.change_bio_flow()
        self.change = self.profile_page.save_changes_is_displayed()
        self.assertTrue(self.change, "Didn't save changes")

    def test_theme_dark_mode(self):
        self.account.click_on_theme_button()
        time.sleep(2)
        self.theme = Theme(self.driver)
        dark_mode = self.theme.click_on_dark_button()
        self.assertTrue(dark_mode, "The mode is not dark")

    def test_theme_light_mode(self):
        self.account.click_on_theme_button()
        time.sleep(2)
        self.theme = Theme(self.driver)
        light_mode = self.theme.click_on_light_button()
        self.assertTrue(light_mode, "The mode is not light")
