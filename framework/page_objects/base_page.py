from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.element.element import Element


class BasePage:

    def __init__(self, driver: Remote):
        self._driver = driver

    def _wait_for_element_to_load(self, element: Element, timeout=10):
        try:
            element_present = EC.presence_of_element_located(element.locator)
            WebDriverWait(self._driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
