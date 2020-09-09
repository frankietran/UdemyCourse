from ..BasePOs.base_page import BasePage
from selenium.webdriver.common.by import By

page_url = "https://accounts.google.com/"
email_input_locator = "input#identifierId"
email_next_button_locator = "div#identifierNext button"
password_input_locator = "input[type='password']"
password_next_button_locator = "div#passwordNext button"


class AuthenticationPopup(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        assert self.is_present(page_url), "Authentication popup page does not exist"

    def enter_email(self, user):
        self.dc.send_keys(user, By.CSS_SELECTOR, email_input_locator)

    def click_email_next(self):
        self.dc.click(By.CSS_SELECTOR, email_next_button_locator)

    def enter_password(self, password):
        self.dc.send_keys(password, By.CSS_SELECTOR, password_input_locator)

    def click_password_next(self):
        self.dc.click(By.CSS_SELECTOR, password_next_button_locator)
