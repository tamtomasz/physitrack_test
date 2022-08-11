from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class ProgramEditorPage(BasePage):

    @property
    def close_link(self) -> Element:
        return Element(By.XPATH, '//a[@id="close-program-editor"]')

    def close(self):
        self._driver.find_element(*self.close_link.locator).click()
