import time

from selenium.webdriver.chrome.options import Options
from behave import use_fixture
from behave.model_core import Status

from seleniumpractice.driver_controller import DriverController
from seleniumpractice.fixture import headless_mode, driver_chrome


def before_feature(context, feature):
    context.options = Options()
    if "fixture.driver.headless" in feature.tags:
        use_fixture(headless_mode, context)
    if "fixture.driver.chrome" in feature.tags:
        use_fixture(driver_chrome, context)
    context.dc = DriverController(context.driver)


def after_step(context, step):
    if step.status == Status.failed:
        context.dc.save_screenshot(context.scenario.name + "_" + step.name + "_" + str(time.time()) + ".png")