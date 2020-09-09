from .base_po import BasePO
from selenium.webdriver.common.by import By


class BaseModal(BasePO):
    def is_present(self, modal_id):
        css_locator = "div#" + modal_id
        return self.dc.get_element(By.CSS_SELECTOR, css_locator) is not None
