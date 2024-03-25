from selenium.webdriver.common.by import By
from Infra.base_page import BasePage
from Utils.scroll import Scroll


class QRCode(BasePage):
    QR_CODE = "//h2[text()='QR Code']"

    def __init__(self, driver):
        super().__init__(driver)
        self.qr_code = self._driver.find_element(By.XPATH, self.QR_CODE)

    def qr_code_is_displayed(self):
        return self.qr_code.is_displayed()
