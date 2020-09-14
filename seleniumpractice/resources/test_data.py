import os
from enum import Enum


google_authentication_popup_url = "https://accounts.google.com/"
email = "frankie@gotitapp.co"
password = ""

problem_des = "Get instant expert help with Excel and Google Sheets"
problem_file_path = os.getcwd() + "/seleniumpractice/resources/sample_problem.png"
directory_path = os.getcwd() + "/seleniumpractice/features/screenshots_failed_steps/"


class PageAttributes(Enum):
    LANDING_URL = 0
    LOGIN_BUTTON_LOCATOR = 1
    HOME_URL = 2


class PageType(Enum):
    ASKER_PORTAL = ["https://www.got-it.io/solutions/excel-chat", "#test-login-button", "https://www.got-it.io/solutions/excel-chat/home"]
    MS_LANDING = ["https://www.got-it.io/partners/excelchat", "#test-login-button", "https://www.got-it.io/partners/excelchat/home"]
    MS_SUPPORT_LANDING = ["https://www.got-it.tech/partners/excelsupport", "#test-login-button", "https://www.got-it.tech/partners/excelsupport/home"]

    LEARNER_PORTAL = ["https://business.learning.got-it.io/courses", ".gi-navBar-Items button", "https://business.learning.got-it.io/my-courses"]
    BYO_LEARNER_PORTAL = ["https://learning.got-it.io/courses", ".gi-navLanding-Link", "https://learning.got-it.io/my-courses"]
