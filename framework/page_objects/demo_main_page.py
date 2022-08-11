from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class DemoMainPage(BasePage):

    @property
    def search_bar(self) -> Element:
        return Element(By.XPATH, '//input[@id="autocomplete-0-input"]')

    @property
    def exercise(self) -> Element:
        return Element(By.XPATH, '//div[@class="list-content-container"]')

    @property
    def add_to_cart_checkbox(self) -> Element:
        return Element(By.XPATH, '//img[@class="cb exercise-checkbox"]')

    @property
    def cart(self) -> Element:
        return Element(By.XPATH, '//div[@class="cart-link-container"]')

    def select_exercise_by_index(self, index: int):
        exercises = self._driver.find_elements(*self.exercise.locator)
        exercise_to_bo_added = exercises[index]
        exercise_to_bo_added.find_element(*self.add_to_cart_checkbox.locator).click()

    def insert_text_into_search_bar(self, text_to_insert: str):
        search_bar = self._driver.find_element(*self.search_bar.locator)
        search_bar.send_keys(text_to_insert)
        search_bar.send_keys(Keys.ENTER)

    def wait_for_items_in_cart(self, expected_number_of_items: int):
        cart_with_items = Element(By.XPATH,
                                  f'//div[@class="nav-counter" and contains(text(), "{expected_number_of_items}")]')
        self._wait_for_element_to_load(cart_with_items)

    def wait_for_cart_to_activate(self):
        self._wait_for_element_to_load(self.cart)

    def click_cart_button(self):
        self._driver.find_element(*self.cart.locator).click()

