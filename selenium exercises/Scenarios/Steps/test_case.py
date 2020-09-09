from ...get_driver import get_driver_by_browser_name
from ...driver_controller import DriverController
from ...POM.Land.landing_page import LandingPage
from ...POM.Land.login_modal import LoginModal
from ...POM.Land.authentication_popup import AuthenticationPopup
from ...POM.Home.home_page import HomePage


user = ""
password = ""


def login_ggl_by_browser_name(browser):
    driver = get_driver_by_browser_name(browser, False)
    dc = DriverController(driver)

    dc.go_to_url("https://www.got-it.ai/solutions/excel-chat/")
    land_page = LandingPage(dc)

    land_page.click_login_button()
    login_modal = LoginModal(dc)

    main_window = dc.get_curr_win()
    handles_before_click = dc.get_all_win_handles()
    login_modal.click_google_icon()
    handles_after_click = dc.get_all_win_handles()

    assert dc.wait_for_new_win(len(handles_before_click))
    for handle in handles_after_click:
        if handle not in handles_before_click:
            dc.switch_to_win(handle)
            popup = AuthenticationPopup(dc)
            popup.enter_email(user)
            popup.click_email_next()
            popup.enter_password(password)
            popup.click_email_next()
            dc.switch_to_win(main_window)

    home_page = HomePage(dc)
    #home_page.post_problem()     #not implemented yet


login_ggl_by_browser_name("chrome")