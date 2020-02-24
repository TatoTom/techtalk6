import subprocess
import time
from dotenv import load_dotenv
from locators import OwnCloudLoginPageLocators
from pages import LoginPage


def docker_compose_up():
    print('Docker compose up ...')
    load_dotenv(dotenv_path='owncloud-docker-server/.env')
    subprocess.run(['docker-compose', '-f', 'owncloud-docker-server/docker-compose.yml', 'up', '-d'],
                   stdout=subprocess.PIPE,
                   universal_newlines=True)
    time.sleep(10)


def docker_compose_down():
    print('Docker compose down ...')
    subprocess.run(['docker-compose', '-f', 'owncloud-docker-server/docker-compose.yml', 'down'],
                   stdout=subprocess.PIPE,
                   universal_newlines=True)
    time.sleep(10)


def test_login_correct_credentials(chrome_browser):
    CORRECT_USERNAME = 'admin'
    CORRECT_PASSWORD = 'admin'

    owncloud = LoginPage(chrome_browser)
    owncloud.login(username=CORRECT_USERNAME, password=CORRECT_PASSWORD)
    logged_user_text = owncloud.get_logged_user_text()

    assert logged_user_text == CORRECT_USERNAME


def test_login_incorrect_credentials(chrome_browser):
    INCORRECT_USERNAME = 'username'
    INCORRECT_PASSWORD = 'qwerty'

    owncloud = LoginPage(chrome_browser)
    owncloud.login(username=INCORRECT_USERNAME, password=INCORRECT_PASSWORD)
    lost_password_text = owncloud.get_lost_password_text()

    assert lost_password_text.strip() == OwnCloudLoginPageLocators.LOST_PASSWORD_INFO_TEXT
