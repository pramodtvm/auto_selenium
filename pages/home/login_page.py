from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "ast-button"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="class")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


    def verify_login_succesful(self):
        result = self.isElementPresent("zl-navbar-rhs-img", "class")
        return result


