import importlib

from framework.web_driver.webdriver_base import WebDriverBaseClass


class WebDriverFactory:

    @staticmethod
    def by_browser_name(browser_name: str) -> WebDriverBaseClass:
        try:
            browser_module = importlib.import_module(f'framework.web_driver.web_browsers.{browser_name}')
            return getattr(browser_module, f'{browser_name.capitalize()}WebDriver')()
        except ModuleNotFoundError:
            raise RuntimeError(f"Browser {browser_name} not defined.")
