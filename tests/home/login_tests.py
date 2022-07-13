from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("t@email.com", "bc")
        result = self.lp.verify_login_succesful()
        assert result == False

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verify_login_succesful()
        assert result == True
