from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWait:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_type, locator, timeout=10, pf=0.5):
        element = None
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pf,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        except:
            print("Time out")
        return element

    def wait_for_url(self, url, timeout=10, pf=0.5):
        wait = WebDriverWait(self.driver, timeout, pf)
        return wait.until(EC.url_to_be(url))

    def wait_for_new_window(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(lambda driver: len(self.driver.window_handles) == 2)

