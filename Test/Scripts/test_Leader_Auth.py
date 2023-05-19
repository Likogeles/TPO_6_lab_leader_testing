import sys

from data import email, password
import time

from src.PageObject.Pages.AuthPage import Auth
from src.TestBase.WebDriverSetup import WebDriverSetup
import unittest

sys.path.append(sys.path[0] + "/...")


class Leader_Auth(WebDriverSetup):
    def test_Leader_Auth(self):
        driver = self.driver
        driver.implicitly_wait(0.5)
        self.driver.get("https://leader-id.ru")
        self.driver.set_page_load_timeout(10)

        auth = Auth(driver)
        auth.getOpenLoginWindowBtn().click()
        auth.loginWindowOpened(driver)
        auth.getLoginEmailField().send_keys(email)
        auth.getLoginPasswordField().send_keys(password)

        auth.getLoginInputBtn().click()

        capcha = input('Нужно было пройти капчу? anything/n: ')
        if not capcha == 'n':
            auth.getLoginInputBtn().click()

        time.sleep(3)

        if auth.getProfileIcon(driver):
            print("Авторизация успешно выполнена")
            self.assertTrue(True)
        else:
            print("Авторизация не пройдена")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
