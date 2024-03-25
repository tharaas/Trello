from selenium.webdriver.common.by import By
from Infra.base_page import BasePage
from Utils.scroll import Scroll


class BoardMenu(BasePage):

    CLOSE_MENU = "//a[contains(@title,'Close the board menu.')]"
    CHANGE_BACKGROUND = "//a[contains(@class,'change-background')]"
    PRINT_QR = "//a[contains(@class,'share')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.scroll = Scroll(driver)
        self.close_menu = self._driver.find_element(By.XPATH, self.CLOSE_MENU)
        self.background = self._driver.find_element(By.XPATH, self.CHANGE_BACKGROUND)
        self.print_qr = self._driver.find_element(By.XPATH, self.PRINT_QR)

    def click_on_close_menu_button(self):
        self.close_menu.click()
        
    def click_on_change_background_button(self):
        self.background.click()

    def click_on_print_qr_button(self):
        self.scroll.scrollHeight()
        self.print_qr.click()


