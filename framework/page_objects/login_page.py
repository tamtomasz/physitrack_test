from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class LoginPage(BasePage):

    @property
    def back_to_demo_button(self) -> Element:
        return Element(By.XPATH, '//a[@class="link-back-to-demo" and contains(text(), "Back to demo")]')

    def click_back_to_demo(self):
        self._driver.find_element(*self.back_to_demo_button.locator).click()
