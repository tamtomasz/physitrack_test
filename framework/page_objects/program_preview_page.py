from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class ProgramPreviewPage(BasePage):

    @property
    def program_code(self) -> Element:
        return Element(By.XPATH, '//div[contains(text(), "Program code:")]//strong')

    @property
    def close_link(self) -> Element:
        return Element(By.XPATH, '//a[@id="assign-progam-modal-cancel"]')

    def wait_for_page_to_load(self):
        self._wait_for_element_to_load(self.program_code)

    def get_program_code(self) -> str:
        return self._driver.find_element(*self.program_code.locator).text

    def close(self):
        self._driver.find_element(*self.close_link.locator).click()
