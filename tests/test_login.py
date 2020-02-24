import subprocess
import time
from selenium import webdriver
from dotenv import load_dotenv


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
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.get('http://localhost:8080')
    user_input = driver.find_element_by_id('user')
    user_input.send_keys('admin')
    password_input = driver.find_element_by_id('password')
    password_input.send_keys('admin')
    submit_button = driver.find_element_by_id('submit')
    submit_button.click()
    display_name = driver.find_element_by_id('expandDisplayName')
    assert display_name.text == 'admin'
    driver.quit()


def test_login_incorrect_credentials():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.get('http://localhost:8080')
    user_input = driver.find_element_by_id('user')
    user_input.send_keys('username')
    password_input = driver.find_element_by_id('password')
    password_input.send_keys('qwerty')
    submit_button = driver.find_element_by_id('submit')
    submit_button.click()
    lost_password = driver.find_element_by_id('lost-password')
    assert lost_password.text.strip() == 'Wrong password. Reset it?'
    driver.quit()
