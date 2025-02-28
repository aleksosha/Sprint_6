import allure
from .base_page import BasePage
from ..locators.second_order_page_locators import SecondOrderPageLocators

class SecondOrderPage(BasePage):

    @allure.step("Открыть календарь")
    def click_calendar(self):
        self.click(SecondOrderPageLocators.CALENDAR_BUTTON)

    @allure.step("Выбрать дату")
    def set_date(self):
        self.click(SecondOrderPageLocators.RENTAL_DATE)

    @allure.step("Выбрать срок аренды")
    def set_rental_period(self):
        self.click(SecondOrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(SecondOrderPageLocators.RENTAL_PERIOD_SEVEN_DAYS_OPTION)

    @allure.step("Выбрать цвет самоката")
    def set_color(self, color):
        self.click(color)

    @allure.step("Добавить комментарий для курьера")
    def set_comment_for_courier(self, comment):
        self.send_keys(SecondOrderPageLocators.COMMENT_FOR_COURIER, comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.click(SecondOrderPageLocators.ORDER_BUTTON)

    @allure.step("Проверить, что заказ подтвержден")
    def is_order_confirmed(self):
        self.wait_for_element(SecondOrderPageLocators.CONFIRMATION_MODAL, timeout=10)
        return self.is_element_displayed(SecondOrderPageLocators.CONFIRMATION_MODAL)
