import allure
from ..locators.first_order_page_locators import FirstOrderPageLocators
from .base_page import BasePage

class FirstOrderPage(BasePage):

    @allure.step("Заполнить поле 'Имя'")
    def set_name(self, name):
        self.send_keys(FirstOrderPageLocators.NAME_INPUT, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def set_last_name(self, last_name):
        self.send_keys(FirstOrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.send_keys(FirstOrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Выбрать станцию метро")
    def choose_metro_station(self):
        self.click(FirstOrderPageLocators.METRO_STATION_INPUT)
        self.click(FirstOrderPageLocators.METRO_STATION_CHOICE)

    @allure.step("Заполнить поле 'Телефон'")
    def set_phone_number(self, phone):
        self.send_keys(FirstOrderPageLocators.PHONE_NUMBER_INPUT, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click(FirstOrderPageLocators.NEXT_PAGE_BUTTON)
