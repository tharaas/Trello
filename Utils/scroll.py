import time

from Logic.UI_Logic.Functional.login_page import LogInPage
from Logic.UI_Logic.Functional.trello_page import TrelloPage


class Scroll:
    def __init__(self, driver):
        self.driver = driver

    def scrollHeight(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
