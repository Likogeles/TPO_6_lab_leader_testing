from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ChangePasswordTest:
    def __init__(self, driver):
        self.driver = driver

    def test(self):
        self.driver.get("https://leader-id.ru/events")
        self.driver.implicitly_wait(0.5)

        # Поле ввода названия
        name_input_field = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/section/div/div[2]/input')
        name_input_field.send_keys("Лагерь")
        print(1)



