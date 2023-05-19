import sys

from src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By


class EventsPageFilter(object):
    def __init__(self, driver):
        self.cards = None
        self.driver = driver
        self.name_input_field = driver.find_element(By.XPATH, Locator.name_input_field)
        self.remove_city_filter_btn = driver.find_element(By.XPATH, Locator.remove_city_events_filter_btn)

    def get_name_input_field(self):
        return self.name_input_field

    def get_cards(self, driver):
        self.cards = driver.find_elements(By.XPATH, Locator.card)
        return self.cards

    def get_remove_city_filter_btn(self):
        return self.remove_city_filter_btn
