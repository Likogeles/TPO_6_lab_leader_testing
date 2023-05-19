import sys
import time

from src.PageObject.Pages.EventsPageFilter import EventsPageFilter
from src.TestBase.WebDriverSetup import WebDriverSetup
import unittest


sys.path.append(sys.path[0] + "/...")


class Leader_EventsPageFilter(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver
        self.driver.get("https://leader-id.ru/events")
        self.driver.set_page_load_timeout(10)

        events = EventsPageFilter(driver)

        text = "Батл Знание.Наука"
        events.get_name_input_field().send_keys(text)
        events.get_remove_city_filter_btn().click()
        time.sleep(3)

        cards = events.get_cards(driver)
        for card in cards:
            if text.lower() in card.text.lower():
                print("Объект найден")
                self.assertTrue(True)
                break
        else:
            print("Объект не найден")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
