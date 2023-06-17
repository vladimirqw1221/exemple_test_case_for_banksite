import pytest

from pages.login_page import LoginClass


class TestLoginPage:
    @pytest.fixture
    def set_up(self, driver):
        set_up = LoginClass(driver, "http://zero.webappsecurity.com/")
        set_up.open()
        return set_up

    def test_login_page_correct_data(self,set_up):
        set_up.login_page()
        set_up.case_check_word_after_login_page()

    def test_incorrect_data_for_login_page(self, set_up):
        set_up.login_for_incorrect_user()
        set_up.quuel_massage_for_incarrect_user()
