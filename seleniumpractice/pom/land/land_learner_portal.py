from seleniumpractice.pom.land.landing_page import LandingPage
from seleniumpractice.resources.test_data import PageType, PageAttributes


class LandPageLearnerPortal(LandingPage):
    page_url = PageType.LEARNER_PORTAL.value[PageAttributes.LANDING_URL.value]
    login_button_locator = PageType.LEARNER_PORTAL.value[PageAttributes.LOGIN_BUTTON_LOCATOR.value]