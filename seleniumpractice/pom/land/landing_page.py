from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_page import BasePage


class LandingPage(BasePage):
    login_button_locator = None

    def click_login_button(self):
        self.dc.click(By.CSS_SELECTOR, self.login_button_locator)