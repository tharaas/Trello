
class BasePage:

    def __init__(self, driver):
        self._driver = driver
        print("start test: ")

    def get_url_driver(self):
        return self._driver.current_url

