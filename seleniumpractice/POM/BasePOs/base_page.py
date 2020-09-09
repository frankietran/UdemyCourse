from selenium.webdriver.common.by import By

from seleniumpractice.POM.BasePOs.base_po import BasePO


class BasePage(BasePO):
    def is_present(self, url):
        return self.dc.has_url(url)
