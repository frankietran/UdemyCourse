from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_page import BasePage
from seleniumpractice.resources.undecided import home_page_url


class HomePage(BasePage):
    page_url = home_page_url
    account_icon_locator = "i[class*='account']"

    problem_des_locator = "div[class*='gi-coverBoxAsk--home'] div textarea"
    browse_file_locator = "div.gi-askForm-FileOption-Upload input[type='file']"
    file_options_locator = "div.gi-coverAskForm-fileResult div label input"
    no_file_index = 0
    upload_file_index = 1
    gglsheet_link_index = 2

    def enter_problem_description(self, problem_des):
        self.dc.click_element(By.CSS_SELECTOR, self.problem_des_locator)
        self.dc.send_keys_to_element(problem_des, By.CSS_SELECTOR, self.problem_des_locator)

    def upload_file(self, problem_file_path):
        self.dc.click_element_from_list_by_index(By.CSS_SELECTOR, self.file_options_locator, self.upload_file_index)
        self.dc.send_keys_to_element(problem_file_path, By.CSS_SELECTOR, self.browse_file_locator)