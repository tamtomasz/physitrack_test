from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class NavigationPage(BasePage):

    @property
    def patients_nav_link(self) -> Element:
        return Element(By.XPATH, '//a[@id="nav-tab-clients"]')

    def click_on_patients_tab(self):
        self._driver.find_element(*self.patients_nav_link.locator).click()
