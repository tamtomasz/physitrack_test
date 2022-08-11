import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from tests.base_test import BaseTest


class TestDemo(BaseTest):

    def _wait_for_element_to_load(self, find_by, value, timeout=10):
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

        # pick USA flag
        self._wait_for_element_to_load(By.XPATH, '//img[@alt="flag_us"]')
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
        self._wait_for_element_to_load(By.XPATH, '//iframe[@title="Tour"]', timeout=30)
        tour_frame = driver.find_element(By.XPATH, '//iframe[@title="Tour"]')
        driver.switch_to.frame(tour_frame)
        skip_tour_button = driver.find_element(By.XPATH, '//p[contains(text(), "Skip tour")]')
        skip_tour_button.click()
        driver.switch_to.default_content()

        # close notifications
        # self._wait_for_element_to_load(By.XPATH, '//iframe[@title="Help Scout Beacon - Messages and Notifications"]',
        #                                timeout=30)
        # notifications_box = driver.find_element(By.XPATH,
        #                                         '//iframe[@title="Help Scout Beacon - Messages and Notifications"]')
        # driver.switch_to.frame(notifications_box)
        # close_notifications_button = driver.find_element(By.XPATH, '//div[@id="BeaconNotifications-root"]')
        # span_to_close = close_notifications_button.find_element(
        #     By.XPATH, '//span[@class="sc-AxgMl cVmQYF c-BeaconCloseButton__label"]')
        # ActionChains(driver).move_to_element(close_notifications_button).perform()
        # ActionChains(driver).move_to_element(span_to_close).click().perform()
        # driver.switch_to.default_content()

        # insert text into search bar
        search_bar = driver.find_element(By.XPATH, '//input[@id="autocomplete-0-input"]')
        search_bar.send_keys("Bird dog")
        search_bar.send_keys(Keys.ENTER)

        # click close tour button
        self._wait_for_element_to_load(By.XPATH, '//iframe[@title="Tour"]')
        tour_frame = driver.find_element(By.XPATH, '//iframe[@title="Tour"]')
        driver.switch_to.frame(tour_frame)
        close_tour_button = driver.find_element(By.XPATH, '//p[contains(text(), "Close")]')
        close_tour_button.click()
        driver.switch_to.default_content()

        # select Bird dog excercise
        exercises = driver.find_elements(By.XPATH, '//div[@class="list-content-container"]')
        exercise_to_bo_added = exercises[0]
        div_with_title = exercise_to_bo_added.find_element(By.XPATH, '//div[@class="lc-text"]')
        link_with_exc_title = div_with_title.find_element(By.TAG_NAME, 'a')
        expected_excrcise_title = link_with_exc_title.get_attribute('title')
        expected_exercise_id = link_with_exc_title.get_attribute('href').split('id=')[1]
        add_checkbox = exercise_to_bo_added.find_element(By.XPATH, '//img[@class="cb exercise-checkbox"]')
        add_checkbox.click()

        # click cart button
        cart_div = driver.find_element(By.XPATH, '//div[@class="cart-link-container"]')
        self._wait_for_element_to_load(By.XPATH, '//div[@class="nav-counter" and contains(text(), "1")]')
        cart_div.click()

        # click on Don't show tour
        self._wait_for_element_to_load(By.XPATH, '//iframe[@title="Tour"]')
        tour_frame = driver.find_element(By.XPATH, '//iframe[@title="Tour"]')
        driver.switch_to.frame(tour_frame)
        dont_show_tour_button = driver.find_element(By.XPATH, '//p[contains(text(), "Don’t show tour")]')
        dont_show_tour_button.click()
        driver.switch_to.default_content()

        # click assign button
        self._wait_for_element_to_load(By.XPATH, '//a[@id="assign-program-modal-button"]')
        assign_link = driver.find_element(By.XPATH, '//a[@id="assign-program-modal-button"]')
        assign_link.click()

        # select patient
        patient_selector_div = driver.find_element(By.XPATH, '//div[contains(@class, "patient-selector")]')
        patient_selector_div.click()
        patient_selector_input = driver.find_element(By.XPATH, '//input[contains(@id, "react-select")]')
        patient_selector_input.send_keys("Demo")
        self._wait_for_element_to_load(By.XPATH, '//div[contains(text(), "Demo-patient")]')
        patient_selector_input.send_keys(Keys.ENTER)

        # assign program to patient
        assign_program_button = driver.find_element(By.XPATH, '//button[@id="assign-protocol-button"]')
        assign_program_button.click()

        # get program code
        new_program_code_div = driver.find_element(By.XPATH, '//div[contains(text(), "Program code:")]')
        new_program_code_str = new_program_code_div.find_element(By.TAG_NAME, 'strong')

        time.sleep(5)
