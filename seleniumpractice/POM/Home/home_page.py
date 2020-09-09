from selenium.webdriver.common.by import By

from seleniumpractice.POM.BasePOs.base_page import BasePage

file_description = "Get instant expert help with Excel and Google Sheets"
file_path = "/foo.png"

account_icon_locator = "i[class*='account']"
page_url = "https://www.got-it.ai/solutions/excel-chat/home"
problem_des_locator = "div[class*='gi-coverBoxAsk--Home'] div textarea"

no_file_index = 1
upload_file_index = 2
gglsheet_link_index = 3
file_option_locator = "div.gi-coverAskForm-fileResult div:nth-child({})"

browse_file_locator = "div.gi-askForm-FileOption-Upload input[type='file']"


class HomePage(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        self.is_present(page_url)

    def enter_problem_description(self):
        self.dc.click(By.CSS_SELECTOR, problem_des_locator)
        self.dc.send_keys(file_description, By.CSS_SELECTOR, problem_des_locator)

    def upload_file(self):
        self.dc.click(By.CSS_SELECTOR, file_option_locator.format(upload_file_index))
        self.dc.send_keys(file_path, By.CSS_SELECTOR, browse_file_locator)
