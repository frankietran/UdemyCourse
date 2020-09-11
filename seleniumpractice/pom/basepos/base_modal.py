from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_po import BasePO


class BaseModal(BasePO):
    ele_container_modal_id = None

    def is_present(self):
        return self.dc.is_element_clickable_after_wait(By.CSS_SELECTOR, self.ele_container_modal_id)
