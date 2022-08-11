from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class CountrySelectionPage(BasePage):

    @property
    def continue_button(self) -> Element:
        return Element(By.XPATH, '//button[contains(text(), "Continue")]')

    def select_flag(self, flag_name: str):
        flag_element = Element(By.XPATH, f'//img[@alt="{flag_name}"]')
        self._wait_for_element_to_load(flag_element)
        flag = self._driver.find_element(*flag_element.locator)
        flag.click()

    def click_continue(self):
        self._driver.find_element(*self.continue_button.locator).click()