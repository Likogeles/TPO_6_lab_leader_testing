import sys

from src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By


class Profile(object):
    def __init__(self, driver):
        self.driver = driver

        self.change_password_btn = None
        self.success_change_password = None
        self.commit_change_password_btn = None
        self.old_password_field = None
        self.new_password_field = None
        self.log_in_button = driver.find_element(By.XPATH, Locator.log_in_button)
        self.password_field = driver.find_element(By.XPATH, Locator.password_field)
        self.email_field = driver.find_element(By.XPATH, Locator.email_field)

    def loginSuccess(self, driver):
        self.change_password_btn = driver.find_element(By.XPATH, Locator.change_password_btn)

    def changePasswordBtnClicked(self, driver):
        self.old_password_field = driver.find_element(By.XPATH, Locator.old_password_field)
        self.new_password_field = driver.find_element(By.XPATH, Locator.new_password_field)
        self.commit_change_password_btn = driver.find_element(By.XPATH, Locator.commit_change_password_btn)

    def newPasswordCommited(self, driver):
        self.success_change_password = driver.find_element(By.XPATH, Locator.success_change_password)

    def getLoginEmailField(self):
        return self.email_field

    def getLoginPasswordField(self):
        return self.password_field

    def getLoginInputBtn(self):
        return self.log_in_button

    def getChangePasswordButton(self):
        return self.change_password_btn

    def getOldPasswordField(self):
        return self.old_password_field

    def getNewPasswordField(self):
        return self.new_password_field

    def getCommitPasswordBtn(self):
        return self.commit_change_password_btn

    def getSuccessChangePassword(self):
        return self.success_change_password
