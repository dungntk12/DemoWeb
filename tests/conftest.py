import pytest

from config.config import TestData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(params=["chrome", "firefox"], scope="class")
@pytest.fixture(params=[ "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        # web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        option = webdriver.ChromeOptions()
        option.add_argument("start-maximized")
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    if request.param == "firefox":
        # web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.close()