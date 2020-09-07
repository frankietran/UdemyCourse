from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class DriverController:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def go_to_url(self, url):
        self.driver.get(url)

    def has_url(self, url, timeout=10, pf=0.5):
        wait = WebDriverWait(self.driver, timeout, pf)
        try:
            wait.until(EC.url_to_be(url))
        except:
            return False
        else:
            return True

    def quit_browser(self):
        self.driver.quit()

    def get_curr_win(self):
        return self.driver.current_window_handle

    def get_all_win_handles(self):
        return self.driver.window_handles

    def switch_to_win(self, win):
        self.driver.switch_to.window(win)

    def wait_for_new_win(self, num_win):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(lambda driver: len(self.driver.window_handles) == num_win+1)

    @staticmethod
    def get_by_type(locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator_type, locator, timeout=10, pf=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pf,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
        except:
            print("Element not found")
        return element

    @staticmethod
    def click(element):
        if element is not None:
            element.click()
        else:
            print("Can't click None element")

    @staticmethod
    def send_keys(element, key):
        if element is not None:
            element.send_keys(key)
        else:
            print("Can't send keys to None element")
