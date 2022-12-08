import pytest

from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest

class Test_ResutlSearch(BaseTest):

    def test_link_selenium_visible(self):
        self.loginPage = LoginPage(self.driver)
        resultSearchPage = self.loginPage.do_search(TestData.TEXT_SEARCH)
        flag = resultSearchPage.is_link_selenium_exist()
        assert  flag