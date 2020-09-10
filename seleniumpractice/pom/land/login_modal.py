from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_modal import BaseModal


class LoginModal(BaseModal):
    ele_container_modal_id = "div#modal-login"
    icons_locator = "div[class ='gi-FormRow'] div:nth-child({}) button"
    linkedin_icon_index = 1
    google_icon_index = 2
    facebook_icon_index = 3

    def click_google_icon(self):
        self.dc.wait_to_click(By.CSS_SELECTOR, self.icons_locator.format(self.google_icon_index))

    def click_linkedin_icon(self):
        self.dc.wait_to_click(By.CSS_SELECTOR, self.icons_locator.format(self.linkedin_icon_index))

    def click_facebook_icon(self):
        self.dc.wait_to_click(By.CSS_SELECTOR, self.icons_locator.format(self.facebook_icon_index))
