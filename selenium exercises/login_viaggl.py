from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from util import ExplicitWait

#google credentials
USER = ""
PASS = ""


driver = webdriver.Chrome(executable_path="drivers/chromedriver")
wait = ExplicitWait(driver)


def set_up():
    driver.get("https://www.got-it.ai/solutions/excel-chat/")
    driver.maximize_window()
    driver.implicitly_wait(5)


def open_login():
    test_login_button = driver.find_element_by_id("test-login-button")
    test_login_button.click()


def open_ggl():
    parent_handle = driver.current_window_handle

    google_icon = wait.wait_for_element(By.XPATH, "//button[text()='Google']")
    google_icon.click()

    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) == 2)
    handles = driver.window_handles

    for handle in handles:
        if handle != parent_handle:
            driver.switch_to.window(handle)
            fill_in_ggl()
            driver.switch_to.window(parent_handle)
            wait.wait_for_url("https://www.got-it.ai/solutions/excel-chat/home")
            print("Sucess")


def fill_in_ggl():
    email = wait.wait_for_element(By.ID, "identifierId", 20)
    email.send_keys(USER)
    driver.find_element_by_id("identifierNext").click()

    password = wait.wait_for_element(By.NAME, "password")
    password.send_keys(PASS)
    driver.find_element_by_id("passwordNext").click()


set_up()
open_login()
open_ggl()
driver.quit()
