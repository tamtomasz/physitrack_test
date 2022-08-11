from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By

from framework.page_objects.country_selection_page import CountrySelectionPage
from framework.page_objects.demo_main_page import DemoMainPage
from framework.page_objects.login_page import LoginPage
from framework.page_objects.main_page import MainPage
from framework.page_objects.navigation_page import NavigationPage
from framework.page_objects.patient_page import PatientPage
from framework.page_objects.patient_selection_page import PatientSelectionPage
from framework.page_objects.patients_list_page import PatientsListPage
from framework.page_objects.popup_page import PopupPage
from framework.page_objects.program_editor_page import ProgramEditorPage
from framework.page_objects.program_page import ProgramPage
from framework.page_objects.program_preview_page import ProgramPreviewPage
from tests.base_test import BaseTest


class TestDemo(BaseTest):

    def test_demo_account_flow(self):
        driver: Remote = self.driver

        # go to home page
        driver.get("https://www.physitrack.co.uk/")

        # click login btn
        main_page = MainPage(driver)
        main_page.click_log_in_button()
        driver.switch_to.window(driver.window_handles[-1])

        # pick USA flag
        country_selection_page = CountrySelectionPage(driver)
        country_selection_page.select_flag('flag_us')

        # click Continue
        country_selection_page.click_continue()

        # click Back to Demo
        login_page = LoginPage(driver)
        login_page.click_back_to_demo()

        # click skip tour button
        tour_popup_page = PopupPage(driver, 'Tour')
        tour_popup_page.click_popup_button('Skip tour')

        # insert text into search bar
        demo_main_page = DemoMainPage(driver)
        demo_main_page.insert_text_into_search_bar("Bird dog")

        # click close tour button
        tour_popup_page.click_popup_button('Close')

        # select Bird dog excercise
        demo_main_page.select_exercise_by_index(0)

        # click cart button
        demo_main_page.wait_for_items_in_cart(1)
        demo_main_page.wait_for_cart_to_activate()
        demo_main_page.click_cart_button()

        # click on Don't show tour
        tour_popup_page.click_popup_button('Don’t show tour')

        # click assign button
        program_page = ProgramPage(driver)
        program_page.wait_for_assign_button()
        program_page.click_assign_button()

        # select patient
        patient_selection_page = PatientSelectionPage(driver)
        patient_selection_page.select_patient('Demo')

        # assign program to patient
        patient_selection_page.click_assign_program_to_patient()

        # get program code
        program_preview_page = ProgramPreviewPage(driver)
        program_preview_page.wait_for_page_to_load()
        new_program_code_str = program_preview_page.get_program_code()

        # close windows
        program_preview_page.close()
        program_editor_page = ProgramEditorPage(driver)
        program_editor_page.close()

        # open patients list
        navigation_page = NavigationPage(driver)
        navigation_page.click_on_patients_tab()

        # click skip tour button
        tour_popup_page.click_popup_button('Skip tour')

        # click on Demo-patient
        patients_list_page = PatientsListPage(driver)
        patients_list_page.click_on_demo_patient()

        # click on Don't show tour
        tour_popup_page.click_popup_button('Don’t show tour')

        # verify program code is correct
        patient_page = PatientPage(driver)
        client_program_selector_div = driver.find_element(*patient_page.client_program_selector_div.locator)
        try:
            client_program_selector_div.find_element(By.XPATH, f'//div[text()="{new_program_code_str}"]')
            print("New program was added successfully to Demo-patient")
            assert True
        except NoSuchElementException:
            print("Failed to add program to Demo-client")
            assert False
