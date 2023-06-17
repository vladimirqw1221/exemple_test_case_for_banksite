import time
import allure
from base_page.base_page import BaseClass
from locators.locators import Locators
from dotenv import load_dotenv
import os


class LoginClass(BaseClass):
    locator = Locators()
    load_dotenv()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def login_page(self):
        with allure.step("Login method"):
            self.select_element_is_clickable(self.locator.SIGN_IN).click()
            self.select_element_is_visibale(self.locator.LOGIN).send_keys(os.getenv('SECRET_USER'))
            self.select_element_is_visibale(self.locator.PAWORD).send_keys(os.getenv('SECRET_PAWORD'))
            self.select_element_is_clickable(self.locator.SIGN_IN_BTN).click()
            self.navigate_to_back()


    def case_check_word_after_login_page(self):
        with allure.step("Check word after login"):
            word = self.select_element_is_visibale(self.locator.ZERO_BANK_IN_HOMO_PAGE)
            self.word_check(word, "Zero Bank")

    def login_for_incorrect_user(self):
        with allure.step("Test invalid data for login page"):
            self.select_element_is_clickable(self.locator.SIGN_IN).click()
            self.select_element_is_visibale(self.locator.LOGIN).send_keys(os.getenv('INCORRECT_UNAME'))
            self.select_element_is_visibale(self.locator.PAWORD).send_keys(os.getenv('SECRET_PAWORD'))
            self.select_element_is_clickable(self.locator.SIGN_IN_BTN).click()

    def quuel_massage_for_incarrect_user(self):
        with allure.step("Check word fo authorization pqge, if user type invalid data"):
            word = self.select_element_is_visibale(self.locator.MSG_INCORRECT)
            self.word_check(word, "Login and/or password are wrong.")








