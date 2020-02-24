import pytest
from selenium import webdriver


@pytest.yield_fixture(scope='function')
def chrome_browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(30)
    chrome_driver.get('http://localhost:8080')
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
