import sys

from src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By


class BoilPointsPageSort(object):
    def __init__(self, driver):
        self.search_city_card = None
        self.search_city_field = None
        self.all_cities_btn = None
        self.driver = driver

        self.remove_city_boil_points_filter_btn = driver.find_element(By.XPATH, Locator.remove_city_boil_points_filter_btn)
        self.download_btn = driver.find_element(By.XPATH, Locator.download_btn)

    def get_download_btn(self):
        return self.download_btn

    def city_filter_removed(self, driver):
        self.all_cities_btn = driver.find_element(By.XPATH, Locator.all_cities_btn)

    def city_list_ready(self, driver):
        self.search_city_field = driver.find_element(By.XPATH, Locator.search_city_field)

    def city_input_ready(self, driver):
        self.search_city_card = driver.find_element(By.XPATH, Locator.search_city_card)

    def get_remove_city_boil_points_filter_btn(self):
        return self.remove_city_boil_points_filter_btn

    def get_cards(self, driver):
        self.cards = driver.find_elements(By.XPATH, Locator.card)
        return self.cards

    def get_remove_city_filter_btn(self):
        return self.remove_city_boil_points_filter_btn

    def get_all_cities_btn(self):
        return self.all_cities_btn

    def get_search_city_field(self):
        return self.search_city_field

    def get_search_city_card(self):
        return self.search_city_card
