from selenium.webdriver.common.by import By

from seleniumpractice.POM.BasePOs.base_po import BasePO


class BaseModal(BasePO):
    def is_present(self, modal_id):
        css_locator = "div#" + modal_id
        return self.dc.get_element(By.CSS_SELECTOR, css_locator) is not None
