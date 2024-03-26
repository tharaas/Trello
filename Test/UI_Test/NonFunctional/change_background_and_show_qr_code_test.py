import unittest
import time

from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_Logic.Functional.board_page import BoardPage
from Logic.UI_Logic.Functional.home_page import HomePage
from Logic.UI_Logic.NonFunctional.background import Background
from Logic.UI_Logic.Functional.board_menu import BoardMenu
from Logic.UI_Logic.NonFunctional.change_background_button import ChangeBackground
from Logic.UI_Logic.NonFunctional.qr_code_button import QRCode
from Logic.UI_Logic.NonFunctional.show_qr_code_button import ShowQRCode
from Utils.login_logout import LoginPageActions
from jira_report import JiraReport


class BoardBackground(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = LoginPageActions(self.driver)
        self.login.fill_email_input_and_go_to_password_sign_in()

        self.home_page = HomePage(self.driver)
        time.sleep(2)
        self.home_page.click_on_board_button()
        self.home_page.click_on_board()
        time.sleep(3)
        self.board_menu = BoardMenu(self.driver)

    def tearDown(self):
        self.driver.quit()
        if hasattr(self, 'assertion_passed') and self.assertion_passed:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_board_change_background"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_board_change_background(self):
        time.sleep(2)
        #self.board_page = BoardPage(self.driver)
        #self.board_page.click_on_menu_button_in_board()
        self.board_menu.click_on_change_background_button()
        self.change_background = ChangeBackground(self.driver)
        self.change_background.click_on_change_background_button()
        time.sleep(2)
        self.background = Background(self.driver)
        self.background.change_background()
        self.change = self.background.background_is_displayed()
        self.assertTrue(self.change, "Background color is not as expected.")

    def test_board_Show_qr_code(self):
        self.board_menu.click_on_print_qr_button()
        self.show_qr = ShowQRCode(self.driver)
        self.show_qr.click_on_show_qr_code()
        time.sleep(2)
        self.qr_code = QRCode(self.driver)
        self.code = self.qr_code.qr_code_is_displayed()
        self.assertTrue(self.code, "QR Code is not as expected.")

