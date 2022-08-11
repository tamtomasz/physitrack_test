from selenium.webdriver.common.by import By

from framework.element.element import Element
from framework.page_objects.base_page import BasePage
from selenium.webdriver import Remote


class PopupPage(BasePage):

    def __init__(self, driver: Remote, iframe_title: str):
        super().__init__(driver)
        self.iframe_title = iframe_title

    @property
    def iframe_element(self) -> Element:
        return Element(By.XPATH, f'//iframe[@title="{self.iframe_title}"]')

    def click_popup_button(self, button_text: str):
        with self.frame_context:
            self._driver.find_element(By.XPATH, f'//p[contains(text(), "{button_text}")]').click()

    @property
    def frame_context(self):
        class PopupContext:

            def __init__(self, popup_page):
                self._popup_page = popup_page

            def __enter__(self):
                self._popup_page._wait_for_element_to_load(self._popup_page.iframe_element, timeout=30)
                frame = self._popup_page._driver.find_element(*self._popup_page.iframe_element.locator)
                self._popup_page._driver.switch_to.frame(frame)

            def __exit__(self, except_type, value, traceback):
                self._popup_page._driver.switch_to.default_content()

        return PopupContext(self)
