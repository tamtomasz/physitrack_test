from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage


class MainPage(BasePage):

    @property
    def login_button(self) -> Element:
        login_button_url = "https://us.physitrack.com/login"
        return Element(By.XPATH, f'//div[@id="top"]//a[@href="{login_button_url}"]')

    def click_log_in_button(self):
        self._driver.find_element(*self.login_button.locator).click()

