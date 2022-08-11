import time

from pytest import fixture
from framework.web_driver.webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser

@fixture
def get_driver(request, get_browser):
    print(f"Selected browser: {get_browser}")
    web_driver = WebDriverFactory.by_browser_name(get_browser)
    web_driver.install()
    _driver = web_driver.driver
    request.cls.driver = _driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()




