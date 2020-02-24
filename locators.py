from selenium.webdriver.common.by import By


class OwnCloudLoginPageLocators:
    """
    Locators for OwnCloud login page
    """
    USERNAME_INPUT_ID = (By.ID, 'user')
    PASSWORD_INPUT_ID = (By.ID, 'password')
    SUBMIT_BUTTON_ID = (By.ID, 'submit')
    LOST_PASSWORD_INFO_ID = (By.ID, 'lost-password')
    LOST_PASSWORD_INFO_TEXT = 'Wrong password. Reset it?'


class OwnCloudMainPageLocators:
    """
    Locators for OwnCloud main page
    """
    USER_DISPLAY_NAME = (By.ID, 'expandDisplayName')
