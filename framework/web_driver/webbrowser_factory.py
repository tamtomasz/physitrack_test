import importlib

from framework.web_driver.webbrowser_base import WebBrowserBaseClass


class WebBrowserFactory:

    @staticmethod
    def by_browser_name(browser_name: str) -> WebBrowserBaseClass:
        try:
            browser_module = importlib.import_module(f'framework.web_driver._wb_{browser_name}')
            return getattr(browser_module, f'{browser_name.capitalize()}WebDriver')()
        except ModuleNotFoundError:
            raise RuntimeError(f"Browser {browser_name} not defined.")
