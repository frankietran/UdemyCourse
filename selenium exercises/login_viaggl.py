from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from util import ExplicitWait


def open_form(driver, wait):
    driver.get("https://www.got-it.ai/solutions/excel-chat/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    test_login_button = driver.find_element(By.ID, "test-login-button")
    test_login_button.click()

    google_icon = wait.wait_for_element(By.XPATH, "//button[text()='Google']")
    google_icon.click()

    wait.wait_for_new_window()


def fill_in(driver, wait, user, pw):
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    email = wait.wait_for_element(By.ID, "identifierId", 20)
    email.send_keys(user)
    driver.find_element(By.ID, "identifierNext").click()

    password = wait.wait_for_element(By.NAME, "password")
    password.send_keys(pw)
    driver.find_element(By.ID, "passwordNext").click()

    driver.switch_to.window(handles[0])


def logged_in(wait):
    wait.wait_for_url("https://www.got-it.ai/solutions/excel-chat/home")
    print("Success")


def main(driver):
    wait = ExplicitWait(driver)

    open_form(driver, wait)
    fill_in(driver, wait, user, pw)
    logged_in(wait)

    driver.quit()


user = ""
pw = ""

"""
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--mute-audio")
chrome_driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=chrome_options)
"""
chrome_driver = webdriver.Chrome(executable_path="drivers/chromedriver")
#safari_driver = webdriver.Safari(executable_path="drivers/safaridriver")

main(chrome_driver)
#main(safari_driver)

