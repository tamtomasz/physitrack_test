from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from framework.web_driver.webdriver_base import WebDriverBaseClass


class ChromeWebDriver(WebDriverBaseClass):

    def __init__(self):
        super().__init__(Chrome, ChromeService, ChromeDriverManager)
