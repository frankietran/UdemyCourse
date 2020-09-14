from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_page import BasePage


class HomePage(BasePage):
    account_icon_locator = "#setting_menu"

    def is_present(self):
        on_right_page = self.dc.does_curr_url_contain(self.page_url)
        account_icon_visible = self.dc.is_element_visible_after_wait(By.CSS_SELECTOR, self.account_icon_locator)
        return on_right_page and account_icon_visible
