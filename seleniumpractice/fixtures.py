from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from behave import fixture


@fixture
def get_driver_by_browser_name(context, browser_name, headless):
    options = Options()
    if headless is True:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--mute-audio")

    browser_name = browser_name.lower()
    if browser_name == "chrome":
        context.driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox(options=options)
    else:
        context.driver = None
        print("Browser not supported")
    yield context.driver
    context.driver.quit()
