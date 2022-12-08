import pytest

from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest

class Test_Login(BaseTest):

    def test_search(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_search(TestData.TEXT_SEARCH)