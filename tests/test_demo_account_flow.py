import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.base_test import BaseTest


class TestDemo(BaseTest):

    def _wait_for_element_to_load(self, find_by, value):
        timeout = 10
        try:
            element_present = EC.presence_of_element_located(
                (find_by, value))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def test_demo_account_flow(self):
        driver: Remote = self.driver

        # go to home page
        driver.get("https://www.physitrack.co.uk/")

        # click login btn
        login_button_url = "https://us.physitrack.com/login"
        navbar_container = driver.find_element(By.XPATH, '//div[@id="top"]')
        login_button = navbar_container.find_element(By.XPATH, f'//a[@href="{login_button_url}"]')
        login_button.click()
        driver.switch_to.window(driver.window_handles[-1])

        self._wait_for_element_to_load(By.XPATH, '//img[@alt="flag_us"]')

        # pick USA flag
        usa_flag = driver.find_element(By.XPATH, '//img[@alt="flag_us"]')
        usa_flag.click()

        # click Continue
        continue_button = driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]')
        continue_button.click()

        # click Back to Demo
        back_to_demo_button = driver.find_element(
            By.XPATH, '//a[@class="link-back-to-demo" and contains(text(), "Back to demo")]')
        back_to_demo_button.click()

        # click skip tour button
        self._wait_for_element_to_load(By.XPATH,  '//iframe[@title="Tour"]')
        tour_frame = driver.find_element(By.XPATH, '//iframe[@title="Tour"]')
        driver.switch_to.frame(tour_frame)
        skip_tour_button = driver.find_element(By.XPATH, '//p[contains(text(), "Skip tour")]')
        skip_tour_button.click()

        time.sleep(5)
