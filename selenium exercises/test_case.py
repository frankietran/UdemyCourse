from selenium import webdriver
from driver_controller import DriverController

user = ""
password = ""


def get_driver_by(browser):
    driver = None
    browser = browser.lower()
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    else:
        print("This browser is not supported")
    return driver


def fill_in_ggl_form(dc):
    email_input = dc.get_element("css", "input#identifierId")
    dc.send_keys(email_input, user)

    email_next = dc.get_element("css", "div#identifierNext button")
    dc.click(email_next)

    password_input = dc.get_element("css", "input[type='password']")
    dc.send_keys(password_input, password)

    password_next = dc.get_element("css", "div#passwordNext button")
    dc.click(password_next)


def verify_land_homepage(dc):
    try:
        assert dc.has_url("https://www.got-it.ai/solutions/excel-chat/home")
        assert (dc.get_element("css", "i[class*='account'") is not None)
    except AssertionError:
        print("Did not land on homepage")
    finally:
        dc.quit_browser()


def login_ggl(dc):
    dc.go_to_url("https://www.got-it.ai/solutions/excel-chat/")

    test_login_button = dc.get_element("css", "button#test-login-button")
    dc.click(test_login_button)

    main_win = dc.get_curr_win()
    open_wins_before = dc.get_all_win_handles()

    #google_icon = dc.get_element("xpath", "//div[class ='gi-FormRow']//button[text()='Google']")
    google_icon = dc.get_element("css", "div[class ='gi-FormRow'] div:nth-child(2) button")
    dc.click(google_icon)

    try:
        dc.wait_for_new_win(len(open_wins_before))
    except TimeoutError:
        print("Google log in window does not open")
    else:
        open_wins_after = dc.get_all_win_handles()
        for win_handle in open_wins_after:
            if win_handle not in open_wins_before:
                dc.switch_to_win(win_handle)
                fill_in_ggl_form(dc)
                dc.switch_to_win(main_win)
                verify_land_homepage(dc)


def login_ggl_by_driver(driver_type):
    driver = get_driver_by(driver_type)
    if driver is not None:
        dc = DriverController(driver)
        login_ggl(dc)


login_ggl_by_driver("chrome")
