import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..locators.second_order_page_locators import SecondOrderPageLocators

class SecondOrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть календарь")
    def click_calendar(self):
        self.driver.find_element(*SecondOrderPageLocators.CALENDAR_BUTTON).click()

    @allure.step("Выбрать дату")
    def set_date(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(SecondOrderPageLocators.RENTAL_DATE)
        ).click()

    @allure.step("Выбрать срок аренды")
    def set_rental_period(self):
        self.driver.find_element(*SecondOrderPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(SecondOrderPageLocators.RENTAL_PERIOD_SEVEN_DAYS_OPTION)
        ).click()

    @allure.step("Выбрать цвет самоката 'Серая безысходность'")
    def set_gray_colour(self):
        self.driver.find_element(*SecondOrderPageLocators.GRAY_HOPELESSNESS).click()

    @allure.step("Добавить комментарий для курьера")
    def set_comment_for_courier(self, comment):
        self.driver.find_element(*SecondOrderPageLocators.COMMENT_FOR_COURIER).send_keys(comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.driver.find_element(*SecondOrderPageLocators.ORDER_BUTTON).click()
