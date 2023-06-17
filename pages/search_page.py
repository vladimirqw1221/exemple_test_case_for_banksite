import time

from selenium.webdriver import Keys
from src.enums.global_enums import GlobalEnums
from locators.locators import Locators
from pages.login_page import LoginClass
import os
from dotenv import load_dotenv
import allure


class SearchPageClass(LoginClass):
    locator = Locators()
    load_dotenv()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def search_bor(self):
        with allure.step("Testing search bar"):
            self.select_element_is_clickable(self.locator.SIGN_IN).click()
            self.select_element_is_visibale(self.locator.LOGIN).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibale(self.locator.PAWORD).send_keys(os.getenv('SECRET_PAWORD'))
            self.select_element_is_clickable(self.locator.SIGN_IN_BTN).click()
            self.navigate_to_back()
            self.select_element_is_visibale(self.locator.SEARCH_BAR).send_keys("Card")
            self.select_element_is_visibale(self.locator.SEARCH_BAR).send_keys(Keys.RETURN)

    def case_word_search_result(self):
        with allure.step("Search result word"):
            word = self.select_element_is_visibale(self.locator.SEARCH_RESULT)
            self.word_check(word, "Search Results:")

    def checking_dropdown(self):
        with allure.step("Check drop down"):
            self.select_element_is_clickable(self.locator.SIGN_IN).click()
            self.select_element_is_visibale(self.locator.LOGIN).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibale(self.locator.PAWORD).send_keys(os.getenv('SECRET_PAWORD'))
            self.select_element_is_clickable(self.locator.SIGN_IN_BTN).click()
            self.navigate_to_back()
            self.select_element_is_clickable(self.locator.DROP_DOWN_LIST).click()
            value_text = self.select_element_is_visibale(self.locator.DROPDOWN_SETTINGS).text
            assert value_text == "Account Settings", GlobalEnums.WRONG_ASSER_ERROR.value
