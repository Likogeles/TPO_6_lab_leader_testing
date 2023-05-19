import sys

from src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By


class UsersPageFilter(object):
    def __init__(self, driver):
        self.leader_cards = None
        self.close_filter_tags_btn = None
        self.filter_tags = None
        self.all_filters_users_btn = None
        self.driver = driver

        self.profile_icon = None
        self.log_in_button = None
        self.password_field = None
        self.email_field = None
        self.driver = driver
        self.open_login_window_btn = driver.find_element(By.XPATH, Locator.open_login_window_btn)

    def login_ready(self, driver):
        self.all_filters_users_btn = driver.find_element(By.XPATH, Locator.all_filters_users_btn)
        self.filter_tags = driver.find_elements(By.XPATH, Locator.filter_tags)
        self.close_filter_tags_btn = driver.find_element(By.XPATH, Locator.close_filter_tags_btn)

    def find_leaders(self, driver):
        self.leader_cards = driver.find_elements(By.XPATH, Locator.leader_cards)
        return self.leader_cards

    def get_close_filter_tags_btn(self):
        return self.close_filter_tags_btn

    def get_filter_tags(self):
        return self.filter_tags

    def get_all_filters_users_btn(self):
        return self.all_filters_users_btn

    def loginWindowOpened(self, driver):
        self.email_field = driver.find_element(By.XPATH, Locator.email_field)
        self.password_field = driver.find_element(By.XPATH, Locator.password_field)
        self.log_in_button = driver.find_element(By.XPATH, Locator.log_in_button)

    def getProfileIcon(self, driver):
        self.profile_icon = driver.find_element(By.XPATH, Locator.profile_icon)
        return self.profile_icon

    def getLoginEmailField(self):
        return self.email_field

    def getLoginPasswordField(self):
        return self.password_field

    def getLoginInputBtn(self):
        return self.log_in_button

    def getOpenLoginWindowBtn(self):
        return self.open_login_window_btn