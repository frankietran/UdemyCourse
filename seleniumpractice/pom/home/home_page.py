from selenium.webdriver.common.by import By

from seleniumpractice.pom.basepos.base_page import BasePage
from seleniumpractice.resources.test_data import home_page_url


class HomePage(BasePage):
    page_url = home_page_url
    account_icon_locator = "#setting_menu"
    try_it_now_button_locator = "section[class='gi-Landing-SectionReadyStart'] div div button"

    problem_des_locator = "div[class='gi-coverBoxAsk gi-coverBoxAsk--Home'] div div textarea"
    file_options_locator = ".gi-coverAskForm-fileResult div:nth-child({}) label"
    no_file_index = 1
    upload_file_index = 2
    gglsheet_link_index = 3
    browse_file_locator = "div.gi-askForm-FileOption-Upload input[type='file']"
    submit_problem_locator = "button#submit-button-payment"

    def is_present(self):
        on_right_page = self.dc.does_curr_url_contain(self.page_url)
        top_element_present = self.dc.is_element_clickable_after_wait(By.CSS_SELECTOR, self.account_icon_locator)
        bottom_element_present = self.dc.is_element_clickable_after_wait(By.CSS_SELECTOR, self.try_it_now_button_locator)
        return on_right_page and top_element_present and bottom_element_present

    def enter_problem_description(self, problem_des):
        self.dc.wait_to_click(By.CSS_SELECTOR, self.problem_des_locator)
        self.dc.send_keys(problem_des, By.CSS_SELECTOR, self.problem_des_locator)

    def upload_file(self, problem_file_path):
        self.dc.wait_to_click(By.CSS_SELECTOR, self.file_options_locator.format(self.upload_file_index))
        self.dc.send_keys(problem_file_path, By.CSS_SELECTOR, self.browse_file_locator)

    def submit_problem(self):
        self.dc.click(By.CSS_SELECTOR, self.submit_problem_locator)
