from selenium.webdriver.common.by import By


class Locators:
    """Login page"""

    SIGN_IN = (By.CSS_SELECTOR, "#signin_button")
    LOGIN = (By.CSS_SELECTOR, '#user_login')
    PAWORD = (By.CSS_SELECTOR, "#user_password")
    SIGN_IN_BTN = (By.XPATH, "//input[@class='btn btn-primary']")

    """Words"""
    ZERO_BANK_IN_HOMO_PAGE = (By.XPATH, "//a[@class='brand']")
    SEARCH_RESULT = (By.CSS_SELECTOR, ".row-divider +h2")
    NAVIGATE_FEEDBACK = (By.CSS_SELECTOR, "#feedback-title")

    """Incorrect logon case"""
    MSG_INCORRECT = (By.XPATH, "//div[@class='alert alert-error']")

    """Search bar test case"""
    SEARCH_BAR = (By.CSS_SELECTOR, "#searchTerm")
    DROPDOWN_SETTINGS = (By.CSS_SELECTOR, ".disabled >a")
    DROP_DOWN_LIST = (By.CSS_SELECTOR, ".dropdown-toggle")

    """Feedback page"""

    FEEDBACK = (By.CSS_SELECTOR, "#feedback")
    YNAME = (By.CSS_SELECTOR, "#name")
    EMAIL = (By.CSS_SELECTOR, "#email")
    SUBJECT = (By.CSS_SELECTOR, "#subject")
    COMMENT_INPUT = (By.CSS_SELECTOR, "#comment")
    SEND_MSG = (By.CSS_SELECTOR, ".pull-right>input")
    TEXT_FEEDBACK = (By.CSS_SELECTOR, ".offset3.span6")
    FEEDBACK_TITLE = (By.CSS_SELECTOR, "#feedback-title")


