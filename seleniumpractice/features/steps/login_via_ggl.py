from behave import *

from seleniumpractice.pom.land.login_modal import LoginModal
from seleniumpractice.pom.land.google_authentication_popup import GoogleAuthenticationPopup
from seleniumpractice.pom.home.choose_package_modal import ChoosePackageModal
from seleniumpractice.pom.home.expert_matching_modal import ExpertMatchingModal

from seleniumpractice.resources.test_data import PageType, PageAttributes
from seleniumpractice.resources.test_data import problem_des
from seleniumpractice.resources.test_data import problem_file_path
from seleniumpractice.resources.test_data import email
from seleniumpractice.resources.test_data import password

import time
from behave import register_type


def parse_page_type(text):
    if text == "ASKER_PORTAL":
        return PageType.ASKER_PORTAL
    elif text == "MS_LANDING":
        return PageType.MS_LANDING
    elif text == "MS_SUPPORT_LANDING":
        return PageType.MS_SUPPORT_LANDING
    elif text == "LEARNER_PORTAL":
        return PageType.LEARNER_PORTAL
    elif text == "BYO_LEARNER_PORTAL":
        return PageType.BYO_LEARNER_PORTAL
    else:
        assert False


register_type(PageType=parse_page_type)


@given('I am on landing page of "{page_type:PageType}"')
def step_impl(context, page_type):
    context.dc.go_to_url(page_type.value[PageAttributes.LANDING_URL.value])
    land_page = context.provider.get_land_page(context.dc, page_type)
    assert land_page.is_present()


@when('I click login button on landing page of "{page_type:PageType}"')
def step_impl(context, page_type):
    land_page = context.provider.get_land_page(context.dc, page_type)
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


@then('I should be on home page of "{page_type:PageType}"')
def step_impl(context, page_type):
    home_page = context.provider.get_home_page(context.dc, page_type)
    time.sleep(10)
    assert home_page.is_present()


@when('I enter problem description on home page of "{page_type:PageType}"')
def step_impl(context, page_type):
    home_page = context.provider.get_home_page(context.dc, page_type)
    home_page.enter_problem_description(problem_des)


@when('upload a problem file on home page of "{page_type:PageType}"')
def step_impl(context, page_type):
    home_page = context.provider.get_home_page(context.dc, page_type)
    home_page.upload_file(problem_file_path)


@when('submit the problem on home page of "{page_type:PageType}"')
def step_impl(context, page_type):
    home_page = context.provider.get_home_page(context.dc, page_type)
    home_page.submit_problem()
    print("")


@then('I should see expert matching modal')
def step_impl(context):
    expert_matching_modal = ExpertMatchingModal(context.dc)
    assert expert_matching_modal.is_present()
