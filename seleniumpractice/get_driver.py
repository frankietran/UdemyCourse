from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions


def get_chrome_driver(headless):
    options = chromeOptions()
    if headless is True:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--mute-audio")
    return webdriver.Chrome(options=options)


def get_firefox_driver(headless):
    options = firefoxOptions()
    if headless is True:
        options.headless = True
    return webdriver.Firefox(options=options)