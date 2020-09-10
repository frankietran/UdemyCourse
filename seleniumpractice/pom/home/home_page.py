from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_page import BasePage
from seleniumpractice.resources.undecided import home_page_url

from selenium.common.exceptions import *


class HomePage(BasePage):
    page_url = home_page_url
    account_icon_locator = "i[class*='account']"

    problem_des_locator = "div[class='gi-coverBoxAsk gi-coverBoxAsk--Home'] div div textarea"
    file_options_locator = "div.gi-coverAskForm-fileResult div:nth-child({}) label input"
    no_file_index = 1
    upload_file_index = 2
    gglsheet_link_index = 3
    browse_file_locator = "div.gi-askForm-FileOption-Upload input[type='file']"
    submit_problem_locator = "button#submit-button-payment"

    def enter_problem_description(self, problem_des):
        self.dc.wait_to_click(By.CSS_SELECTOR, self.problem_des_locator, 20, 2)
        self.dc.send_keys(problem_des, By.CSS_SELECTOR, self.problem_des_locator)

    def upload_file(self, problem_file_path):
        self.dc.wait_to_send_keys(By.CSS_SELECTOR, self.file_options_locator.format(self.upload_file_index), 20, 2)
        self.dc.wait_to_send_keys(problem_file_path, By.CSS_SELECTOR, self.browse_file_locator)

    def submit_problem(self):
        self.dc.click(By.CSS_SELECTOR, self.submit_problem_locator)
