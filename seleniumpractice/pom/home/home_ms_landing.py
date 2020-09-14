from selenium.webdriver.common.by import By

from seleniumpractice.pom.home.home_page import HomePage
from seleniumpractice.resources.test_data import PageType, PageAttributes


class HomePageMSLanding(HomePage):
    page_url = PageType.MS_LANDING.value[PageAttributes.HOME_URL.value]
    problem_des_locator = "div[class='gi-coverBoxAsk gi-coverBoxAsk--Home'] div div textarea"
    file_options_locator = ".gi-coverAskForm-fileResult div:nth-child({}) label"
    no_file_index = 1
    upload_file_index = 2
    gglsheet_link_index = 3
    browse_file_locator = "div.gi-askForm-FileOption-Upload input[type='file']"
    submit_problem_locator = "button#submit-button-free"

    def enter_problem_description(self, problem_des):
        self.dc.click(By.CSS_SELECTOR, self.problem_des_locator)
        self.dc.send_keys(problem_des, By.CSS_SELECTOR, self.problem_des_locator)

    def upload_file(self, problem_file_path):
        self.dc.click(By.CSS_SELECTOR, self.file_options_locator.format(self.upload_file_index))
        self.dc.send_keys(problem_file_path, By.CSS_SELECTOR, self.browse_file_locator)

    def submit_problem(self):
        self.dc.click(By.CSS_SELECTOR, self.submit_problem_locator)
