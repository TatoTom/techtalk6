import subprocess
import time
from selenium import webdriver
from dotenv import load_dotenv
from locators import OwnCloudLoginPageLocators, OwnCloudMainPageLocators


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


def test_login_correct_credentials():
    CORRECT_USERNAME = 'admin'
    CORRECT_PASSWORD = 'admin'
    OWNCLOUD_URL = 'http://localhost:8080'

    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.get(OWNCLOUD_URL)
    user_input = driver.find_element(*OwnCloudLoginPageLocators.USERNAME_INPUT_ID)
    user_input.send_keys(CORRECT_USERNAME)
    password_input = driver.find_element(*OwnCloudLoginPageLocators.PASSWORD_INPUT_ID)
    password_input.send_keys(CORRECT_PASSWORD)
    submit_button = driver.find_element(*OwnCloudLoginPageLocators.SUBMIT_BUTTON_ID)
    submit_button.click()
    display_name = driver.find_element(*OwnCloudMainPageLocators.USER_DISPLAY_NAME)
    assert display_name.text == CORRECT_USERNAME
    driver.quit()


def test_login_incorrect_credentials():
    INCORRECT_USERNAME = 'username'
    INCORRECT_PASSWORD = 'qwerty'
    OWNCLOUD_URL = 'http://localhost:8080'

    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.get(OWNCLOUD_URL)
    user_input = driver.find_element(*OwnCloudLoginPageLocators.USERNAME_INPUT_ID)
    user_input.send_keys(INCORRECT_USERNAME)
    password_input = driver.find_element(*OwnCloudLoginPageLocators.PASSWORD_INPUT_ID)
    password_input.send_keys(INCORRECT_PASSWORD)
    submit_button = driver.find_element(*OwnCloudLoginPageLocators.SUBMIT_BUTTON_ID)
    submit_button.click()
    lost_password = driver.find_element(*OwnCloudLoginPageLocators.LOST_PASSWORD_INFO_ID)
    assert lost_password.text.strip() == OwnCloudLoginPageLocators.LOST_PASSWORD_INFO_TEXT
    driver.quit()
