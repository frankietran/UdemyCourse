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

    def wait_for_new_win(self, num_win):
        wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)
        try:
            wait.until(lambda driver: len(self.driver.window_handles) >= num_win+1)
        except TimeoutException:
            return False
        return True

    def wait_for_element_to_be_available(self, by_type, locator, timeout=10, pf=1):
        wait = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=pf)
        try:
            wait.until(EC.element_to_be_clickable((by_type, locator)))
        except TimeoutException:
            return False
        return True

    def get_elements(self, by_type, locator):
        elements = self.driver.find_elements(by_type, locator)
        if len(elements) == 0:
            print("No element found")
        return elements

    def get_element(self, by_type, locator):
        element = None
        try:
            element = self.driver.find_element(by_type, locator)
        except NoSuchElementException:
            print("Element not found")
        return element

    def click_element(self, by_type, locator):
        element = self.get_element(by_type, locator)
        if element is None:
            print("Can't click None element")
        else:
            element.click()

    def click_element_from_list_by_index(self, by_type, locator, index):
        elements = self.get_element(by_type, locator)
        try:
            element = elements[index]
        except IndexError:
            print("Can't be click element not found")
        else:
            element.click()

    def send_keys_to_element(self, key, by_type, locator):
        element = self.get_element(by_type, locator)
        if element is None:
            print("Can't send keys to element not found")
        else:
            element.send_keys(key)

    def send_keys_to_element_from_list_by_index(self, key, by_type, locator, index):
        elements = self.get_element(by_type, locator)
        try:
            element = elements[index]
        except IndexError:
            print("Can't send keys to element not found")
        else:
            element.send_keys(key)

    def save_screenshot(self, filename):
        filepath = "/screenshots_failed_steps/" + filename
        self.driver.save_screenshot(filepath)
