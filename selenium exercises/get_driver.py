from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver_by_browser_name(browser, headless):
    #work on headless
    """
    if headless is True:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--mute-audio")
    """
    driver = None
    browser = browser.lower()
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="Drivers/chromedriver")
        #driver = webdriver.Chrome(executable_path="Drivers/chromedriver", options=options)
    assert driver is not None, "This browser is not supported"
    return driver