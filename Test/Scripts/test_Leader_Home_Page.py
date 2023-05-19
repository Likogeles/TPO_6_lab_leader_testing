import sys
from src.TestBase.WebDriverSetup import WebDriverSetup
import unittest

sys.path.append(sys.path[0] + "/...")


class Leader_HomePage(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver
        self.driver.get("https://leader-id.ru/")
        self.driver.set_page_load_timeout(10)

        web_page_title = "Leader-ID"

        try:
            if driver.title == web_page_title:
                print("\nСтраница успешно загружена")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "Ошибка при загрузке страницы")


if __name__ == '__main__':
    unittest.main()
