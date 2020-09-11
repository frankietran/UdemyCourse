from behave import fixture

from seleniumpractice.get_driver import get_chrome_driver
from seleniumpractice.get_driver import get_firefox_driver
from seleniumpractice.driver_controller import DriverController


@fixture
def browser_chrome(context, headless):
    context.driver = get_chrome_driver(headless)
    context.dc = DriverController(context.driver)
    yield context.driver
    context.driver.quit()


@fixture
def browser_firefox(context, headless):
    context.driver = get_firefox_driver(headless)
    context.dc = DriverController(context.driver)
    yield context.driver
    context.driver.quit()
