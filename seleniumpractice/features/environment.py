import time

from behave import use_fixture
from behave.model_core import Status

from seleniumpractice.driver_controller import DriverController
from seleniumpractice.fixtures import get_driver_by_browser_name


def before_tag(context, tag):
    t = tag.split(".")
    if t[0] == "fixture":
        if t[1] == "browser":
            browser_name = t[2]
            try:
                t[3]
            except IndexError:
                headless = False
            else:
                headless = True
            use_fixture(get_driver_by_browser_name, context, browser_name, headless)
            context.dc = DriverController(context.driver)


def after_step(context, step):
    if step.status == Status.failed:
        context.dc.save_screenshot(context.scenario.name + "_" + step.name + "_" + str(time.time()) + ".png")
