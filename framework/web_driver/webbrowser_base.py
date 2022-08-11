from typing import Optional

from selenium.webdriver import Remote
from selenium.webdriver.common.service import Service
from webdriver_manager.core.manager import DriverManager


class WebBrowserBaseClass:

    def __new__(cls, *args, **kwargs):
        if cls is WebBrowserBaseClass:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, web_browser_driver: Remote.__class__, web_browser_service: Service.__class__,
                 web_browser_driver_manager: DriverManager.__class__):
        self._driver_path: Optional[str] = None
        self._web_browser_driver = web_browser_driver
        self._web_browser_service = web_browser_service
        self._web_browser_driver_manager = web_browser_driver_manager

    def install_driver(self):
        self._driver_path = self._web_browser_driver_manager().install()

    @property
    def driver(self) -> Remote:
        if self._driver_path:
            return self._web_browser_driver(service=self._web_browser_service(self._driver_path))
        else:
            raise RuntimeError("Driver path not found")
