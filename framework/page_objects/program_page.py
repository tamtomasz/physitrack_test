from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class ProgramPage(BasePage):

    @property
    def assign_button(self) -> Element:
        return Element(By.XPATH, '//a[@id="assign-program-modal-button"]')

    def wait_for_assign_button(self):
        self._wait_for_element_to_load(self.assign_button)

    def click_assign_button(self):
        self._driver.find_element(*self.assign_button.locator).click()
