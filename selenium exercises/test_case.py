from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from driver_controller import DriverController
from pom.page_objects import *


user = ""
password = ""


def get_driver_by_browser_name(browser, headless):
    #work on headless
    """
    if headless is True:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--mute-audio")
    """
    driver = None
    browser = browser.lower()
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver")
        #driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=options)
    assert driver is not None, "This browser is not supported"
    return driver


def login_ggl_by_browser_name(browser):
    driver = get_driver_by_browser_name(browser, False)
    dc = DriverController(driver)
    base_page = BasePage(dc)
    land_page = LandingPage(dc)
    login_modal = LoginModal(dc)
    popup_email = AuthenticationPopupEmail(dc)
    popup_password = AuthenticationPopupPassword(dc)
    home_page = HomePage(dc)

    base_page.go_to_url("")     #not implemented yet
    assert land_page.is_present()

    land_page.click_login_button()
    assert login_modal.is_present()

    login_modal.click_google_icon()
    base_page.switch()       #not implemented yet

    assert popup_email.is_present()
    popup_email.enter_email(user)
    popup_email.click_email_next()

    assert popup_password.is_present()
    popup_password.enter_password()
    popup_password.click_email_next()

    base_page.switch()       #not implemented yet
    assert home_page.is_present()
    home_page.post_problem()     #not implemented yet


login_ggl_by_browser_name("chrome")