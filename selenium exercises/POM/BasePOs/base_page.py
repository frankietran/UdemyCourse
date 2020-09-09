from .base_po import BasePO
from selenium.webdriver.common.by import By


class BasePage(BasePO):
    def is_present(self, url):
        return self.dc.has_url(url)
