from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from framework.web_driver.webdriver_base import WebDriverBaseClass


class FirefoxWebDriver(WebDriverBaseClass):

    def __init__(self):
        super().__init__(Firefox, FirefoxService, GeckoDriverManager)
