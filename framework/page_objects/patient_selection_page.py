from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class PatientSelectionPage(BasePage):

    @property
    def assign_program_button(self) -> Element:
        return Element(By.XPATH, '//button[@id="assign-protocol-button"]')

    @property
    def patient_selector_div(self) -> Element:
        return Element(By.XPATH, '//div[contains(@class, "patient-selector")]')

    @property
    def patient_selector_input(self) -> Element:
        return Element(By.XPATH, '//input[contains(@id, "react-select")]')

    def select_patient(self, patient_partial_name: str):
        self._driver.find_element(*self.patient_selector_div.locator).click()
        patient_input = self._driver.find_element(*self.patient_selector_input.locator)
        patient_input.send_keys(patient_partial_name)
        patient_row = Element(
            By.XPATH, f'//div[contains(text(), "{patient_partial_name}") and contains(@class, "react-select__option")]')
        self._wait_for_element_to_load(patient_row)
        self._driver.find_element(*patient_row.locator).click()

    def click_assign_program_to_patient(self):
        self._wait_for_element_to_load(self.assign_program_button)
        self._driver.find_element(*self.assign_program_button.locator).click()
