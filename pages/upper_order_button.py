import allure
from ..locators.upper_order_button_locators import UpperBasePageLocators
from .base_page import BasePage

class UpperOrderButtonPage(BasePage):

    @allure.step('Кликаем по кнопке "Заказать"')
    def click_upper_order_button(self):
        self.click(UpperBasePageLocators.UPPER_ORDER_BUTTON)
        self.is_element_displayed(UpperBasePageLocators.BIKE_FOR_WHOM)
        assert "/order" in self.get_current_url(), "URL не содержит /order"

    @allure.step('Проверяем, что страница заказа открыта')
    def is_order_page_opened(self):
        try:
            element_displayed = self.is_element_displayed(UpperBasePageLocators.BIKE_FOR_WHOM)
            return element_displayed and self.get_current_url() == "https://qa-scooter.praktikum-services.ru/order"
        except Exception:
            return False
