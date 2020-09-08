from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverController:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def go_to_url(self, url):
        self.driver.get(url)

    def has_url(self, url, timeout=10, pf=1):
        wait = WebDriverWait(driver=self.driver, timeout= timeout, poll_frequency= pf)
        try:
            wait.until(EC.url_contains(url))
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
        wait = WebDriverWait(driver=self.driver, timeout= 10, poll_frequency= 1)
        return wait.until(lambda driver: len(self.driver.window_handles) >= num_win+1)

    def get_element(self, by_type, locator, timeout=10, pf=1):
        element = None
        try:
            wait = WebDriverWait(driver=self.driver, timeout= timeout, poll_frequency= pf)
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
        except:
            print("Element not found")
        return element

    def click(self, by_type, locator, timeout=10, pf=1):
        element = self.get_element(by_type, locator, timeout, pf)
        if element is None:
            print("Can't click None element")
        else:
            element.click()

    def send_keys(self, key, by_type, locator, timeout=10, pf=1):
        element = self.get_element(by_type, locator, timeout, pf)
        if element is None:
            print("Can't send keys to None element")
        else:
            element.send_keys(key)

    def is_element_present(self, by_type, locator, timeout=10, pf=1):
        return self.get_element(by_type, locator, timeout, pf) is not None

