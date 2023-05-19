import sys

sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find_element(By.CLASS_NAME, Locator.logo)
        self.search = driver.find_element(By.ID, Locator.search)
        self.log_in = driver.find_element(By.CLASS_NAME, Locator.log_in)
        self.name = driver.find_element(By.NAME, Locator.login)
        self.password = driver.find_element(By.NAME, Locator.password)
        self.log_in_button = driver.find_element(By.XPATH, Locator.log_in_button)

    def getSort(self, id):
        return self.driver.find_element(By.XPATH, Locator.getSort(self, id))

    def getNavigation(self, id):
        return self.driver.find_element(By.XPATH, Locator.getNavigation(self, id))

    def getSelection(self, col, id):
        return self.driver.find_element(By.XPATH, Locator.getSelection(self, col, id))

    def getAuth(self):
        return self.driver.find_element(By.CLASS_NAME, "btn-login").text

    def getSearch(self):
        return self.driver.find_element(By.CLASS_NAME, "berrors").text

    def getSearchPos(self):
        return self.driver.find_element(By.CLASS_NAME, "berrors").text

    def getResult(self, word):
        results = self.driver.find_elements(By.CLASS_NAME, "th-title")
        for result in results:
            if word.lower() in result.text.lower():
                return True
        return False

