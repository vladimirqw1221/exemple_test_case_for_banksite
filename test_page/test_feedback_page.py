import pytest

from pages.feedback_page import FeeadbackClass


class TestFeedback:
    @pytest.fixture
    def set_up(self,driver):
        set_up = FeeadbackClass(driver, "http://zero.webappsecurity.com/")
        set_up.open()
        return set_up

    def test_feedback_page(self,set_up):
        set_up.feedback_case()