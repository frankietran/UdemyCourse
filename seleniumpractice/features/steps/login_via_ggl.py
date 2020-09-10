from behave import *

from seleniumpractice.pom.land.landing_page import LandingPage
from seleniumpractice.pom.land.login_modal import LoginModal
from seleniumpractice.pom.land.google_authentication_popup import GoogleAuthenticationPopup
from seleniumpractice.pom.home.home_page import HomePage
from seleniumpractice.pom.home.choose_package_modal import ChoosePackageModal

from seleniumpractice.resources.undecided import landing_page_url
from seleniumpractice.resources.undecided import problem_des
from seleniumpractice.resources.undecided import problem_file_path
from seleniumpractice.resources.undecided import email
from seleniumpractice.resources.undecided import password


@given('user is on landing page')
def step_impl(context):
    context.dc.go_to_url(landing_page_url)
    LandingPage(context.dc)


@when('user clicks login button on landing page')
def step_impl(context):
    land_page = LandingPage(context.dc)
    land_page.click_login_button()


@then('user sees login modal')
def step_impl(context):
    LoginModal(context.dc)


@when('user clicks Google icon in login modal')
def step_impl(context):
    login_modal = LoginModal(context.dc)
    context.main_window = context.dc.get_curr_win()                    # save handle to switch back to main window later
    context.handles_before_click = context.dc.get_all_win_handles()    # save window handles before click to detect new window
    login_modal.click_google_icon()


@then('user sees a new window')
def step_impl(context):
    assert context.dc.wait_for_new_win(context.handles_before_click)


@when('user switches to the Google authentication window')
def step_impl(context):
    handles_after_click = context.dc.get_all_win_handles()
    for handle in handles_after_click:
        if handle not in context.handles_before_click:
            context.dc.switch_to_win(handle)
            GoogleAuthenticationPopup(context.dc)


@when('user successfully follows through Google authentication process in Google authentication window')
def step_impl(context):
    popup = GoogleAuthenticationPopup(context.dc)
    popup.enter_email(email)
    popup.click_email_next()
    popup.enter_password(password)
    popup.click_password_next()


@when('user switches back to the main window')
def step_impl(context):
    context.dc.switch_to_win(context.main_window)


@then('user is on home page')
def step_impl(context):
    HomePage(context.dc)


@when('user enters problem description and uploads a problem file on home page and submits the problem')
def step_impl(context):
    home_page = HomePage(context.dc)
    home_page.enter_problem_description(problem_des)
    home_page.upload_file(problem_file_path)
    home_page.submit_problem()


@then('user sees choose package modal')
def step_impl(context):
    ChoosePackageModal(context.dc)
