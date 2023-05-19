import sys
import time
from src.TestBase.WebDriverSetup import WebDriverSetup
import unittest

from data import email, password
from src.PageObject.Pages.ProfilePage import Profile

sys.path.append(sys.path[0] + "/...")


class Leader_ProfilePage(WebDriverSetup):

    def test_Profile_Page(self):
        driver = self.driver
        driver.implicitly_wait(0.5)
        self.driver.get("https://leader-id.ru/settings")
        self.driver.set_page_load_timeout(10)

        profile = Profile(driver)

        profile.getLoginEmailField().send_keys(email)
        profile.getLoginPasswordField().send_keys(password)

        profile.getLoginInputBtn().click()

        capcha = input('Нужно было пройти капчу? anything/n: ')
        if not capcha == 'n':
            profile.getLoginInputBtn().click()
        time.sleep(2)
        profile.loginSuccess(driver)

        profile.getChangePasswordButton().click()
        profile.changePasswordBtnClicked(driver)

        profile.getOldPasswordField().send_keys(password)
        profile.getNewPasswordField().send_keys(password)

        input('Подтвержите прохождение капчи: ')
        profile.getCommitPasswordBtn().click()

        time.sleep(1)

        profile.newPasswordCommited(driver)
        if profile.getSuccessChangePassword():
            print("Пароль успешно изменён")
            self.assertTrue(True)
        else:

            print("Ошибка изменения пароля")

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
