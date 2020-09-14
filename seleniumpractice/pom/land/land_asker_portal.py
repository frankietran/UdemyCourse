from seleniumpractice.pom.land.landing_page import LandingPage
from seleniumpractice.resources.test_data import PageType, PageAttributes


class LandPageAskerPortal(LandingPage):
    page_url = PageType.ASKER_PORTAL.value[PageAttributes.LANDING_URL.value]
    login_button_locator = PageType.ASKER_PORTAL.value[PageAttributes.LOGIN_BUTTON_LOCATOR.value]
