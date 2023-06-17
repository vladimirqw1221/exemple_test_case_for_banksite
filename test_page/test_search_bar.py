import pytest

from pages.search_page import SearchPageClass


class TestSearchBar:

    @pytest.fixture
    def set_up(self, driver):
        set_up = SearchPageClass(driver, "http://zero.webappsecurity.com/")
        set_up.open()
        return set_up

    def test_search_box(self, set_up):
        set_up.search_bor()
        set_up.case_word_search_result()

    def test_drop_down(self, set_up):
        set_up.checking_dropdown()

