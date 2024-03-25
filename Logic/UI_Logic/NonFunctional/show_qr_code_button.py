from selenium.webdriver.common.by import By
from Infra.base_page import BasePage
from Utils.scroll import Scroll


class ShowQRCode(BasePage):
    SHOW_QR_CODE = "//a[text()='Show QR Code']"

    def __init__(self, driver):
        super().__init__(driver)
        self.show_qr_code = self._driver.find_element(By.XPATH, self.SHOW_QR_CODE)

    def click_on_show_qr_code(self):
        self.show_qr_code.click()
