import time

from behave.fixture import use_fixture_by_tag
from behave.model_core import Status

from seleniumpractice.pom.provider import Provider
from seleniumpractice.features.steps.fixtures import browser_chrome
from seleniumpractice.features.steps.fixtures import browser_firefox
from seleniumpractice.resources.test_data import directory_path


fixture_registry = {
    "fixture.browser.chrome": (browser_chrome, (), dict(headless=False)),
    "fixture.browser.firefox": (browser_firefox, (), dict(headless=False)),
    "fixture.browser.chrome.headless": (browser_chrome, (), dict(headless=True)),
    "fixture.browser.firefox.headless": (browser_firefox, (), dict(headless=True)),
}


def before_all(context):
    context.provider = Provider()


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)


def after_step(context, step):
    if step.status == Status.failed:
        file_name = context.scenario.name + "_" + step.name + "_" + str(time.time()) + ".png"
        context.dc.save_screenshot(directory_path, file_name)
