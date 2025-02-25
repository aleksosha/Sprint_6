
import allure
from .base_page import BasePage
from ..locators.yandex_button_locators import YandexButtonLocators

class YandexButton(BasePage):

    @allure.step("Кликаем на кнопку Yandex")
    def click_yandex_button(self):
        self.wait_for_element_to_be_clickable(YandexButtonLocators.YANDEX_BUTTON)
        self.click(YandexButtonLocators.YANDEX_BUTTON)

    @allure.step("Переключаемся на новое окно и проверяем URL")
    def switch_to_new_window_and_check_url(self, expected_url):
        self.switch_to_new_window()
        return self.wait_for_url(expected_url)
