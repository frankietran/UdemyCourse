from seleniumpractice.resources.test_data import PageType
from seleniumpractice.pom.land.land_asker_portal import LandPageAskerPortal
from seleniumpractice.pom.land.land_ms_landing import LandPageMSLanding
from seleniumpractice.pom.land.land_ms_support_landing import LandPageMSSupportLanding
from seleniumpractice.pom.land.land_learner_portal import LandPageLearnerPortal
from seleniumpractice.pom.land.land_byo_learner_portal import LandPageByoLearnerPortal
from seleniumpractice.pom.home.home_asker_portal import HomePageAskerPortal
from seleniumpractice.pom.home.home_ms_landing import HomePageMSLanding
from seleniumpractice.pom.home.home_ms_support_landing import HomePageMSSupportLanding
from seleniumpractice.pom.home.home_learner_portal import HomePageLearnerPortal
from seleniumpractice.pom.home.home_byo_learner_portal import HomePageByoLearnerPortal


class Provider:
    @staticmethod
    def get_land_page(driver_controller, page_type):
        if page_type == PageType.ASKER_PORTAL:
            return LandPageAskerPortal(driver_controller)
        elif page_type == PageType.MS_LANDING:
            return LandPageMSLanding(driver_controller)
        elif page_type == PageType.MS_LANDING:
            return LandPageMSSupportLanding(driver_controller)
        elif page_type == PageType.LEARNER_PORTAL:
            return LandPageLearnerPortal(driver_controller)
        elif page_type == PageType.BYO_LEARNER_PORTAL:
            return LandPageByoLearnerPortal(driver_controller)
        else:
            assert False, "Land Page not supported"

    @staticmethod
    def get_home_page(driver_controller, page_type):
        if page_type == PageType.ASKER_PORTAL:
            return HomePageAskerPortal(driver_controller)
        elif page_type == PageType.MS_LANDING:
            return HomePageMSLanding(driver_controller)
        elif page_type == PageType.MS_LANDING:
            return HomePageMSSupportLanding(driver_controller)
        elif page_type == PageType.LEARNER_PORTAL:
            return HomePageLearnerPortal(driver_controller)
        elif page_type == PageType.BYO_LEARNER_PORTAL:
            return HomePageByoLearnerPortal(driver_controller)
        else:
            assert False, "Home Page not supported"
