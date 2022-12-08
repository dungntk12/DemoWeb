from selenium.webdriver.common.by import  By

from config.config import TestData
from pages.BasePage import BasePage
from pages.ResultSearchPage import ResultSearchPage


class LoginPage(BasePage):
    # By locator
    TXTB_SEARCH = (By.NAME, "q")

    # constructor
    def __init__(self, driver) :
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page action
    def do_search(self, text):
        self.do_send_keys(self.TXTB_SEARCH, text)
        return ResultSearchPage(self.driver)