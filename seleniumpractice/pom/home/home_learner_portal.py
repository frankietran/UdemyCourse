from selenium.webdriver.common.by import By

from seleniumpractice.pom.home.home_page import HomePage
from seleniumpractice.resources.test_data import PageType, PageAttributes


class HomePageLearnerPortal(HomePage):
    page_url = PageType.LEARNER_PORTAL.value[PageAttributes.HOME_URL.value]
    logout_option_locator = ".gi-navBar-Account ul[role='menu'] li:nth-child(2) a"

    def log_out(self):
        self.dc.click(By.CSS_SELECTOR, self.account_icon_locator)
        self.dc.click(By.CSS_SELECTOR, self.logout_option_locator)