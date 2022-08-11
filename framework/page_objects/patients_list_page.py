from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class PatientsListPage(BasePage):

    @property
    def patients_row(self) -> Element:
        return Element(By.XPATH, '//div[contains(@id, "ClientListContainer-react-component")]')

    def click_on_demo_patient(self):
        patients_rows = self._driver.find_elements(*self.patients_row.locator)
        for row in patients_rows:
            text_element = row.find_element(By.TAG_NAME, 'strong')
            if text_element.text == "Demo-patient":
                text_element.click()
                return
