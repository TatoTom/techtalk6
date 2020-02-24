import subprocess
import time
from dotenv import load_dotenv
import pytest
from selenium import webdriver


@pytest.yield_fixture(scope='session')
def compose():
    print('\nDocker compose up ...')
    load_dotenv(dotenv_path='owncloud-docker-server/.env')
    subprocess.run(['docker-compose', '-f', 'owncloud-docker-server/docker-compose.yml', 'up', '-d'],
                   stdout=subprocess.PIPE,
                   universal_newlines=True)
    time.sleep(10)
    yield

    print('\nDocker compose down ...')
    subprocess.run(['docker-compose', '-f', 'owncloud-docker-server/docker-compose.yml', 'down'],
                   stdout=subprocess.PIPE,
                   universal_newlines=True)
    time.sleep(10)


@pytest.yield_fixture(scope='function')
def chrome_browser(compose):
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(30)
    chrome_driver.get('http://localhost:8080')
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
