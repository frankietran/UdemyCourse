from ..BasePOs.base_page import BasePage
from selenium.webdriver.common.by import By


account_icon_locator = "i[class*='account']"
page_url = "https://www.got-it.ai/solutions/excel-chat/home"


class HomePage(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        self.is_present(page_url)

    """
    add attribute and methods to support posting a problem, check if submitted 
    """