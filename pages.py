from locators import OwnCloudLoginPageLocators, OwnCloudMainPageLocators


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def login(self, username, password):
        user_input = self.driver.find_element(*OwnCloudLoginPageLocators.USERNAME_INPUT_ID)
        user_input.send_keys(username)
        password_input = self.driver.find_element(*OwnCloudLoginPageLocators.PASSWORD_INPUT_ID)
        password_input.send_keys(password)
        submit_button = self.driver.find_element(*OwnCloudLoginPageLocators.SUBMIT_BUTTON_ID)
        submit_button.click()
