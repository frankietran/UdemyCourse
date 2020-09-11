from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverController:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def go_to_url(self, url):
        self.driver.get(url)

    def does_curr_url_contain(self, url, timeout=10, pf=1):
        wait = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=pf)
        wait.until(EC.url_contains(url))
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
        wait.until(EC.new_window_is_opened(current_handles))

    def is_element_clickable_after_wait(self, by_type, locator, timeout=10, pf=1):
        wait = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=pf)
        wait.until(EC.element_to_be_clickable((by_type, locator)))
        return True

    def get_element(self, by_type, locator):
        return self.driver.find_element(by_type, locator)

    def click(self, by_type, locator):
        element = self.get_element(by_type, locator)
        element.click()

    def wait_to_click(self, by_type, locator, timeout=10, pf=1):
        self.is_element_clickable_after_wait(by_type, locator, timeout, pf)
        self.click(by_type, locator)

    def send_keys(self, key, by_type, locator):
        element = self.get_element(by_type, locator)
        element.send_keys(key)

    def wait_to_send_keys(self, key, by_type, locator, timeout=10, pf=1):
        self.is_element_clickable_after_wait(by_type, locator, timeout, pf)
        self.send_keys(key, by_type, locator)

    def save_screenshot(self, directory_path, file_name):
        file_path = directory_path + file_name
        self.driver.save_screenshot(file_path)
