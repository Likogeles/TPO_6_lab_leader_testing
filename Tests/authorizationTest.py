from selenium.webdriver.common.by import By
import time


class AuthorizationTest:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, email, password):
        self.driver.get("https://leader-id.ru/")
        self.driver.implicitly_wait(0.5)

        login_icon = self.driver.find_element(by=By.CLASS_NAME, value="login-button")
        login_icon.click()

        email_input = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div[4]/div/div/div[2]/div[2]/div/div/span/div[1]/div/span/div/input')
        email_input.send_keys(email)

        password_input = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div[4]/div/div/div[2]/div[2]/div/div/span/div[2]/span/div/input')
        password_input.send_keys(password)

        submit_btn = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div[4]/div/div/div[2]/div[2]/div/div/span/div[4]/button')
        submit_btn.click()
