import time

from Logic.UI_Logic.Functional.account_menu import AccountMenu
from Logic.UI_Logic.Functional.board_page import BoardPage
from Logic.UI_Logic.Functional.home_page import HomePage
from Logic.UI_Logic.Functional.login_page import LogInPage
from Logic.UI_Logic.Functional.trello_page import TrelloPage


class LoginPageActions:
    def __init__(self, driver):
        self.driver = driver

    def fill_email_input_and_go_to_password_sign_in(self):
        self.trello_page = TrelloPage(self.driver)
        self.trello_page.click_on_log_in_button()
        time.sleep(2)
        self.login_page = LogInPage(self.driver)
        self.login_page.login_button_is_displayed()
        self.login_page.fill_email_input_and_go_to_password_sign_in_with_google()
        time.sleep(3)

    def logout_from_open_email(self):
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_account_button()
        self.account = AccountMenu(self.driver)
        self.account.click_on_logout_button()
