from seleniumpractice.pom.land.landing_page import LandingPage
from seleniumpractice.resources.test_data import PageType, PageAttributes


class LandPageMSSupportLanding(LandingPage):
    page_url = PageType.MS_SUPPORT_LANDING.value[PageAttributes.LANDING_URL.value]
    login_button_locator = PageType.MS_SUPPORT_LANDING.value[PageAttributes.LOGIN_BUTTON_LOCATOR.value]
