from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from framework.web_driver.webbrowser_base import WebBrowserBaseClass


class ChromeWebDriver(WebBrowserBaseClass):

    def __init__(self):
        super().__init__(Chrome, ChromeService, ChromeDriverManager)
