from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from framework.web_driver.webbrowser_base import WebBrowserBaseClass


class FirefoxWebDriver(WebBrowserBaseClass):

    def __init__(self):
        super().__init__(Firefox, FirefoxService, GeckoDriverManager)
