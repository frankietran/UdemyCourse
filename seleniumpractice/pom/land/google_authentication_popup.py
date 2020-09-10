from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_page import BasePage
from seleniumpractice.resources.undecided import google_authentication_popup_url


class GoogleAuthenticationPopup(BasePage):
    page_url = google_authentication_popup_url
    email_input_locator = "input#identifierId"
    email_next_button_locator = "div#identifierNext button"
    password_input_locator = "input[type='password']"
    password_next_button_locator = "div#passwordNext button"

    def enter_email(self, email):
        self.dc.wait_to_send_keys(email, By.CSS_SELECTOR, self.email_input_locator)

    def click_email_next(self):
        self.dc.click(By.CSS_SELECTOR, self.email_next_button_locator)

    def switched_to_password_screen(self):
        assert self.dc.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.password_input_locator)

    def enter_password(self, password):
        self.dc.wait_to_send_keys(password, By.CSS_SELECTOR, self.password_input_locator)

    def click_password_next(self):
        self.dc.click(By.CSS_SELECTOR, self.password_next_button_locator)
