from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from src.enums.global_enums import GlobalEnums


class BaseClass:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    """Open browser"""

    def open(self):
        self.driver.get(self.url)
        open_url = self.driver.current_url
        print(f"Browser open {open_url}")

    """Method select element on page"""

    def select_element_is_visibale(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def select_element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def select_elements_is_all_visibale(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def select_element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    """Js helper"""

    def scroll_viev_to_element(self, element):
        return self.driver.execute_script('argument[0].scrollViewTo;', element)

    """Current url """

    def getting_current_url(self):
        value_url = self.driver.current_url
        print(f'Getting current url: {value_url}')

    """Navigate to back"""

    def navigate_to_back(self):
        self.driver.back()
        print("<-: Navigate to back")

    """Assert word """

    def word_check(self, word, result):
        value_word = word.text
        assert value_word == result, GlobalEnums.WRONG_ASSER_ERROR.value
        print(" Word on page correct")

    """Refresh page"""

    def refresh_page(self):
        self.driver.refresh()
        print("Your page refresh")
