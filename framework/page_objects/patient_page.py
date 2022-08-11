from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class PatientPage(BasePage):

    @property
    def client_program_selector_div(self) -> Element:
        return Element(By.XPATH, '//div[contains(@class, "client-program-selector")]')
