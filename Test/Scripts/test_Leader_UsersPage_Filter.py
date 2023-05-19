import sys
import time

from data import password, email
from src.PageObject.Pages.UsersPageFilter import UsersPageFilter
from src.TestBase.WebDriverSetup import WebDriverSetup
import unittest


sys.path.append(sys.path[0] + "/...")


class Leader_UsersFilter(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver
        self.driver.get("https://leader-id.ru/users")
        self.driver.set_page_load_timeout(10)

        users = UsersPageFilter(driver)

        users.getOpenLoginWindowBtn().click()
        users.loginWindowOpened(driver)
        users.getLoginEmailField().send_keys(email)
        users.getLoginPasswordField().send_keys(password)

        users.getLoginInputBtn().click()

        capcha = input('Нужно было пройти капчу? anything/n: ')
        if not capcha == 'n':
            users.getLoginInputBtn().click()

        users.login_ready(driver)
        users.get_all_filters_users_btn().click()

        for tag in users.get_filter_tags():
            tag.click()

        users.get_close_filter_tags_btn().click()

        time.sleep(5)

        name = "Хребтов Александр Валентинович"
        cards = users.find_leaders(driver)
        for card in cards:
            if name.lower() in card.text.lower():
                print("Участники найдены")
                self.assertTrue(True)
                break
        else:
            print("Участники не найдены")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
