from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage

class ResultSearchPage(BasePage):
    # By locator
    LINK_SELENIUM_PYTHON = (By.PARTIAL_LINK_TEXT, "User Guide")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Page action
    def is_link_selenium_exist(self):
        return self.is_visible(self.LINK_SELENIUM_PYTHON)