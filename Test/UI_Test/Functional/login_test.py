import unittest

from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_Logic.Functional.home_page import HomePage
from Utils.login_logout import LoginPageActions


class TrelloLoginTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()

    def tearDown(self):
        self.login.logout_from_open_email()
        self.driver.quit()
        self.driver.close()

    def test_click_on_login_flow(self):
        self.login = LoginPageActions(self.driver)
        self.login.fill_email_input_and_go_to_password_sign_in()
        self.home_page = HomePage(self.driver)
        account_login = self.home_page.account_button_is_displayed()
        self.assertTrue(account_login, "Login was not successful")
