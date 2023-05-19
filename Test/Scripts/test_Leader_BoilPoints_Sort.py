import sys
import time

from src.PageObject.Pages.BoilPointsPageSort import BoilPointsPageSort
from src.PageObject.Pages.EventsPageFilter import EventsPageFilter
from src.TestBase.WebDriverSetup import WebDriverSetup
import unittest


sys.path.append(sys.path[0] + "/...")


class Leader_BoilPointsPageSort(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver
        self.driver.get("https://leader-id.ru/places")
        self.driver.set_page_load_timeout(10)

        boilPoints = BoilPointsPageSort(driver)
        boilPoints.get_download_btn().click()

        # boilPoints.get_remove_city_boil_points_filter_btn().click()
        # boilPoints.city_filter_removed(driver)
        # boilPoints.get_all_cities_btn().click()
        # boilPoints.city_list_ready(driver)
        # city_name = "Ульяновская область"
        # # boilPoints.get_search_city_field().send_keys(city_name)
        # boilPoints.city_input_ready(driver)
        # boilPoints.get_search_city_card().click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
