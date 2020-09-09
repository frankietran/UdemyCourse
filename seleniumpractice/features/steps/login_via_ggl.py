from behave import *

from seleniumpractice.POM.Land.landing_page import LandingPage
from seleniumpractice.POM.Land.login_modal import LoginModal
from seleniumpractice.POM.Land.authentication_popup import AuthenticationPopup
from seleniumpractice.POM.Home.home_page import HomePage
from seleniumpractice.POM.Home.choose_package_modal import ChoosePackageModal


email = ""
password = ""


@given('user is at landing page')
def step_impl(context):
    context.dc.go_to_url("https://www.got-it.ai/solutions/excel-chat/")
    context.land_page = LandingPage(context.dc)


@when('user clicks login button')
def step_impl(context):
    context.land_page.click_login_button()


@then('user sees login modal')
def step_impl(context):
    context.login_modal = LoginModal(context.dc)


@when('user clicks google icon in login modal')
def step_impl(context):
    context.main_window = context.dc.get_curr_win()
    context.handles_before_click = context.dc.get_all_win_handles()
    context.login_modal.click_google_icon()


@then('user sees a new authentication window')
def step_impl(context):
    assert context.dc.wait_for_new_win(len(context.handles_before_click))


@when('user switches to the new window')
def step_impl(context):
    handles_after_click = context.dc.get_all_win_handles()
    for handle in handles_after_click:
        if handle not in context.handles_before_click:
            context.dc.switch_to_win(handle)
            context.popup = AuthenticationPopup(context.dc)


@when('user fills in correct credentials')
def step_impl(context):
    context.popup.enter_email(email)
    context.popup.click_email_next()
    context.popup.enter_password(password)
    context.popup.click_email_next()


@when('user switches back to the main window')
def step_impl(context):
    context.dc.switch_to_win(context.dc.main_window)


@then('user is at home page')
def step_impl(context):
    context.home_page = HomePage(context.dc)


@when('user posts a problem')
def step_impl(context):
    context.home_page.enter_problem_description()
    context.home_page.upload_file()


@then('user sees choose package modal')
def step_impl(context):
    context.login_modal = ChoosePackageModal(context.dc)
