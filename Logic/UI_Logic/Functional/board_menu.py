from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage
from Utils.scroll import Scroll


class BoardMenu(BasePage):
    CLOSE_MENU = "//a[contains(@title,'Close the board menu.')]"
    CHANGE_BACKGROUND = "//a[contains(@class,'change-background')]"
    PRINT_QR = "//a[contains(@class,'share')]"
    CLOSE_BOARD_BUTTON = "//a[contains(@class,'close-board')]"
    CLOSE_BUTTON = "//input[contains(@type,'submit')]"
    DELETE_BOARD = "//button[text()='Permanently delete board']"
    DELETE = "//button[text()='Delete']"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.scroll = Scroll(driver)
        self.close_menu = self._driver.find_element(By.XPATH, self.CLOSE_MENU)
        self.background = self._driver.find_element(By.XPATH, self.CHANGE_BACKGROUND)
        self.print_qr = self._driver.find_element(By.XPATH, self.PRINT_QR)
        self.close_board_button = self._driver.find_element(By.XPATH, self.CLOSE_BOARD_BUTTON)

    def click_on_close_menu_button(self):
        self.close_menu.click()

    def click_on_change_background_button(self):
        self.background.click()

    def click_on_print_qr_button(self):
        self.scroll.scrollHeight()
        self.print_qr.click()

    def click_on_close_board_button(self):
        self.close_board_button.click()

    def close_boutton(self):
        self.close_boutton = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.CLOSE_BUTTON)))
        self.close_boutton.click()

    def click_on_delete_board_button(self):
        self.delete_board_boutton = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.DELETE_BOARD)))
        self.delete_board_boutton.click()

    def click_on_delete(self):
        self.delete = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.DELETE)))
        self.delete.click()

    def delete_board(self):
        self.click_on_close_board_button()
        self.close_boutton()
        self.click_on_delete_board_button()
        self.click_on_delete()
