from ..BasePOs.base_modal import BaseModal
from selenium.webdriver.common.by import By

linkedin_icon_index = 0
google_icon_index = 1
facebook_icon_index = 2
icon_locator = "div[class ='gi-FormRow'] div:nth-child({}) button"
modal_id = "modal-login"


class LoginModal(BaseModal):
    def __init__(self, driver_controller):
        BaseModal.__init__(self, driver_controller)
        assert self.is_present(modal_id), "Login modal does not exist"

    def click_google_icon(self):
        self.dc.click(By.CSS_SELECTOR, icon_locator.format(google_icon_index))

    def click_linkedin_icon(self):
        self.dc.click(By.CSS_SELECTOR, icon_locator.format(linkedin_icon_index))

    def click_facebook_icon(self):
        self.dc.click(By.CSS_SELECTOR, icon_locator.format(facebook_icon_index))
