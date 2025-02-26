import allure
from selenium.webdriver.common.by import By
from ..locators.down_order_button_locators import DownBasePageLocators
from .base_page import BasePage

class DownOrderButtonPage(BasePage):

    @allure.step('Скроллим страницу до кнопки "Заказать"')
    def scroll_to_order_button(self):
        self.scroll_to_element(DownBasePageLocators.ORDER_BUTTON)

    @allure.step('Кликаем по кнопке "Заказать"')
    def click_down_order_button(self):
        self.scroll_to_order_button()
        self.click(DownBasePageLocators.ORDER_BUTTON)

    @allure.step('Проверяем, что страница заказа открыта')
    def is_order_page_opened(self):
        element_displayed = self.is_element_displayed(DownBasePageLocators.ORDER_PAGE_HEADER)
        return element_displayed and self.driver.current_url.startswith(
            'https://qa-scooter.praktikum-services.ru/orders'
        )
