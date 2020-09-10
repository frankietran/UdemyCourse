from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class DriverController:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_for_url_that_contains(self, url, timeout=10, pf=1):
        wait = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=pf)
        try:
            wait.until(EC.url_contains(url))
        except TimeoutException:
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

    def wait_for_new_win(self, current_handles):
        wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)
        try:
            wait.until(EC.new_window_is_opened(current_handles))
        except TimeoutException:
            return False
        return True

    def wait_for_element_to_be_clickable(self, by_type, locator, timeout=10, pf=1):
        wait = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=pf,
                             ignored_exceptions=ElementNotInteractableException)
        try:
            wait.until(EC.element_to_be_clickable((by_type, locator)))
        except TimeoutException:
            print("Can't wait for element to be clickable")
            return False
        return True

    def get_element(self, by_type, locator):
        element = None
        try:
            element = self.driver.find_element(by_type, locator)
        except NoSuchElementException:
            print("Element not found")
        return element

    def click(self, by_type, locator):
        element = self.get_element(by_type, locator)
        if element is None:
            print("Can't click None element")
        else:
            element.click()

    def wait_to_click(self, by_type, locator, timeout=10, pf=1):
        assert self.wait_for_element_to_be_clickable(by_type, locator, timeout, pf)
        element = self.get_element(by_type, locator)
        if element is None:
            print("Can't click None element")
        else:
            element.click()

    def send_keys(self, key, by_type, locator):
        element = self.get_element(by_type, locator)
        if element is None:
            print("Can't send keys to element not found")
        else:
            element.send_keys(key)

    def wait_to_send_keys(self, key, by_type, locator, timeout=10, pf=1):
        assert self.wait_for_element_to_be_clickable(by_type, locator, timeout, pf)
        element = self.get_element(by_type, locator)
        if element is None:
            print("Can't send keys to element not found")
        else:
            element.send_keys(key)

    def save_screenshot(self, filename):
        filepath = "/screenshots_failed_steps/" + filename
        self.driver.save_screenshot(filepath)
