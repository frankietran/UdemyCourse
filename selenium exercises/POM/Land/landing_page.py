from ..BasePOs.base_page import BasePage
from selenium.webdriver.common.by import By


page_url = "https://www.got-it.ai/solutions/excel-chat/"
login_button_locator = "button#test-login-button"


class LandingPage(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        assert self.is_present(page_url), "Landing page does not exist"

    def click_login_button(self):
        self.dc.click(By.CSS_SELECTOR, login_button_locator)
