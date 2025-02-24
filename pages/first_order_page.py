import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..locators.first_order_page_locators import FirstOrderPageLocators

class FirstOrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнить поле 'Имя'")
    def set_name(self, name):
        self.driver.find_element(*FirstOrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step("Заполнить поле 'Фамилия'")
    def set_last_name(self, last_name):
        self.driver.find_element(*FirstOrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.driver.find_element(*FirstOrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step("Выбрать станцию метро")
    def choose_metro_station(self):
        self.driver.find_element(*FirstOrderPageLocators.METRO_STATION_INPUT).click()
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(FirstOrderPageLocators.METRO_STATION_CHOICE)
        ).click()

    @allure.step("Заполнить поле 'Телефон'")
    def set_phone_number(self, phone):
        self.driver.find_element(*FirstOrderPageLocators.PHONE_NUMBER_INPUT).send_keys(phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.driver.find_element(*FirstOrderPageLocators.NEXT_PAGE_BUTTON).click()
