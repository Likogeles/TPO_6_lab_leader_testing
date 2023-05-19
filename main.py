from selenium import webdriver
from selenium.webdriver.common.by import By

import data
from Tests.changePasswordTest import ChangePasswordTest
from Tests.authorizationTest import AuthorizationTest

email = data.email
password = data.password

driver = webdriver.Chrome()

authorizationTest = AuthorizationTest(driver)
authorizationTest.authorization(email, password)

changePasswordTest = ChangePasswordTest(driver)
changePasswordTest.test()


driver.quit()


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")

    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()
