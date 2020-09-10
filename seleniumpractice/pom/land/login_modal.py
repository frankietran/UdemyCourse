from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_modal import BaseModal


class LoginModal(BaseModal):
    ele_container_modal_id = "div#modal-login"

    icons_locator = "div[class ='gi-FormRow'] div button"
    linkedin_icon_index = 0
    google_icon_index = 1
    facebook_icon_index = 2

    def click_google_icon(self):
        self.dc.click_element_from_list_by_index(By.CSS_SELECTOR, self.icons_locator, self.google_icon_index)

    def click_linkedin_icon(self):
        self.dc.click_element(By.CSS_SELECTOR, self.icons_locator, self.linkedin_icon_index)

    def click_facebook_icon(self):
        self.dc.click_element(By.CSS_SELECTOR, self.icons_locator, self.facebook_icon_index)
