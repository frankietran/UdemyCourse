from selenium import webdriver
from behave import fixture

@fixture
def headless_mode(context):
    context.options.add_argument("--headless")
    context.options.add_argument("--disable-gpu")
    context.options.add_argument("--no-sandbox")
    context.options.add_argument("--window-size=1920x1080")
    context.options.add_argument("--mute-audio")
    yield context.options


@fixture
def driver_chrome(context):
    context.driver = webdriver.Chrome(options=context.options)
    assert context.driver is not None, "This browser is not supported"
    yield context.driver
    context.driver.quit()
