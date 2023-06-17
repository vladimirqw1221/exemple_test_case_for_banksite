import time

from locators.locators import Locators
from pages.search_page import SearchPageClass
import allure
from dotenv import load_dotenv
import os
from src.enums.global_enums import GlobalEnums
from generate_peron.generator import generator



class FeeadbackClass(SearchPageClass):
    locator = Locators()
    load_dotenv()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def feedback_case(self):
        with allure.step("Check feedback"):
            person_data = next(generator())
            first_name = person_data.first_name
            zipcode = person_data.zip_code
            email = person_data.email
            self.select_element_is_clickable(self.locator.SIGN_IN).click()
            self.select_element_is_visibale(self.locator.LOGIN).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibale(self.locator.PAWORD).send_keys(os.getenv('SECRET_PAWORD'))
            self.select_element_is_clickable(self.locator.SIGN_IN_BTN).click()
            self.navigate_to_back()
            self.select_element_is_clickable(self.locator.FEEDBACK).click()
            value_feedback = self.select_element_is_visibale(self.locator.NAVIGATE_FEEDBACK).text

            assert value_feedback == "Feedback", GlobalEnums.WRONG_ASSER_ERROR.value

            self.select_element_is_visibale(self.locator.YNAME).send_keys(first_name)
            self.select_element_is_visibale(self.locator.EMAIL).send_keys(email)
            self.select_element_is_visibale(self.locator.SUBJECT).send_keys(zipcode)
            self.select_element_is_visibale(self.locator.COMMENT_INPUT).send_keys("Test test test")
            self.select_element_is_clickable(self.locator.SEND_MSG).click()
            time.sleep(5)
            value_word = self.select_element_is_visibale(self.locator.FEEDBACK_TITLE).text

            assert value_word == "Feedback", GlobalEnums.WRONG_ASSER_ERROR.value

