from behave import *

from seleniumpractice.pom.land.landing_page import LandingPage
from seleniumpractice.pom.land.login_modal import LoginModal
from seleniumpractice.pom.land.google_authentication_popup import GoogleAuthenticationPopup
from seleniumpractice.pom.home.home_page import HomePage
from seleniumpractice.pom.home.choose_package_modal import ChoosePackageModal

from seleniumpractice.resources.test_data import landing_page_url
from seleniumpractice.resources.test_data import problem_des
from seleniumpractice.resources.test_data import problem_file_path
from seleniumpractice.resources.test_data import email
from seleniumpractice.resources.test_data import password


@given('I am on landing page')
def step_impl(context):
    context.dc.go_to_url(landing_page_url)
    land_page = LandingPage(context.dc)
    assert land_page.is_present()


@when('I click login button on landing page')
def step_impl(context):
    land_page = LandingPage(context.dc)
    land_page.click_login_button()


@then('I should see login modal')
def step_impl(context):
    login_modal = LoginModal(context.dc)
    assert login_modal.is_present()


@given('I click Google icon in login modal')
def step_impl(context):
    login_modal = LoginModal(context.dc)
    context.main_window = context.dc.get_curr_win()                    # save handle to switch back to main window later
    context.handles_before_click = context.dc.get_all_win_handles()    # save window handles before click to detect new window
    login_modal.click_google_icon()


@when('a new Google authentication window pops up')
def step_impl(context):
    context.dc.wait_for_new_win(context.handles_before_click)


@then('I should be able to switch to the Google authentication window')
def step_impl(context):
    handles_after_click = context.dc.get_all_win_handles()
    for handle in handles_after_click:
        if handle not in context.handles_before_click:
            context.dc.switch_to_win(handle)
            popup = GoogleAuthenticationPopup(context.dc)
            assert popup.is_present()
            return


@given('I successfully follow through Google authentication process in Google authentication window')
def step_impl(context):
    popup = GoogleAuthenticationPopup(context.dc)
    popup.enter_email(email)
    popup.click_email_next()
    popup.enter_password(password)
    popup.click_password_next()


@when('I switch back to the main window')
def step_impl(context):
    context.dc.switch_to_win(context.main_window)


@then('I should be on home page')
def step_impl(context):
    home_page = HomePage(context.dc)
    assert home_page.is_present()


@when('I enter problem description on home page')
def step_impl(context):
    home_page = HomePage(context.dc)
    home_page.enter_problem_description(problem_des)


@when('upload a problem file')
def step_impl(context):
    home_page = HomePage(context.dc)
    home_page.upload_file(problem_file_path)


@when('submit the problem')
def step_impl(context):
    home_page = HomePage(context.dc)
    home_page.submit_problem()


@then('I should see choose package modal')
def step_impl(context):
    choose_package_modal = ChoosePackageModal(context.dc)
    assert choose_package_modal.is_present()
