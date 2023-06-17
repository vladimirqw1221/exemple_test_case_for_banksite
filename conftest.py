import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    proxy_patch = "23.254.161.181:80"
    options = Options()
    options.add_argument(f'--proxy-server={proxy_patch}')
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    print("\nStart test")
    yield driver
    driver.close()
    driver.quit()
    print("\nFinish test")
