from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_page import BasePage
from seleniumpractice.resources.test_data import landing_page_url


class LandingPage(BasePage):
    page_url = landing_page_url
    login_button_locator = "button#test-login-button"

    def click_login_button(self):
        self.dc.click(By.CSS_SELECTOR, self.login_button_locator)
