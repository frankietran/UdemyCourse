from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver_controller):
        self.dc = driver_controller

    def is_present(self):
        pass


class LandingPage(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        self.login_button_locator = "button#test-login-button"

    def is_present(self):
        on_the_right_page = self.dc.has_url("https://www.got-it.ai/solutions/excel-chat/")
        elements_present = self.dc.get_element(By.CSS_SELECTOR, self.login_button_locator) is not None
        return on_the_right_page and elements_present

    def click_login_button(self):
        self.dc.click(By.CSS_SELECTOR, self.login_button_locator)


class LoginModal(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        self.google_icon_locator = "div[class ='gi-FormRow'] div:nth-child(2) button"

    def is_present(self):
        on_the_right_page = self.dc.has_url("https://www.got-it.ai/solutions/excel-chat/")
        #add later: check if div.modal-dialog is present
        elements_present = self.dc.get_element(By.CSS_SELECTOR, self.google_icon_locator) is not None
        return on_the_right_page and elements_present

    def click_google_icon(self):
        self.dc.click(By.CSS_SELECTOR, self.google_icon_locator)


class AuthenticationPopupEmail(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        self.email_input_locator = "input#identifierId"
        self.next_button_locator = "div#identifierNext button"

    def is_present(self):
        on_the_right_page = self.dc.has_url("https://accounts.google.com/")

        email_input_present = self.dc.get_element(By.CSS_SELECTOR, self.email_input_locator) is not None
        next_button_present = self.dc.get_element(By.CSS_SELECTOR, self.next_button_locator) is not None
        elements_present = email_input_present and next_button_present

        return on_the_right_page and elements_present

    def enter_email(self, user):
        self.dc.send_keys(user, By.CSS_SELECTOR, self.email_input_locator)

    def click_email_next(self):
        self.dc.click(By.CSS_SELECTOR, self.next_button_locator)


class AuthenticationPopupPassword(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        self.password_input_locator = "input[type='password']"
        self.next_button_locator = "div#passwordNext button"

    def is_present(self):
        on_the_right_page = self.dc.has_url("https://accounts.google.com/")

        pass_input_present = self.dc.get_element(By.CSS_SELECTOR, self.password_input_locator) is not None
        next_button_present = self.dc.get_element(By.CSS_SELECTOR, self.next_button_locator) is not None
        elements_present = pass_input_present and next_button_present

        return on_the_right_page and elements_present

    def enter_password(self, password):
        self.dc.send_keys(password, By.CSS_SELECTOR, self.password_input_locator)

    def click_password_next(self):
        self.dc.click(By.CSS_SELECTOR, self.next_button_locator)


class HomePage(BasePage):
    def __init__(self, driver_controller):
        BasePage.__init__(self, driver_controller)
        self.account_icon_locator = "i[class*='account']"

    def is_present(self):
        on_the_right_page = self.dc.has_url("https://www.got-it.ai/solutions/excel-chat/home")
        elements_present = self.dc.get_element(By.CSS_SELECTOR, self.account_icon_locator) is not None
        return on_the_right_page and elements_present
    """
    add attribute and methods to support posting a problem, check if submitted 
    """