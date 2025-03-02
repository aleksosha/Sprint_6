import allure
from ..locators.confirm_order_locators import ConfirmOrderLocators
from .base_page import BasePage

class ConfirmOrderPage(BasePage):
    @allure.step("Ожидание появления окна подтверждения")
    def wait_for_modal(self):
        self.wait_for_element(ConfirmOrderLocators.MODAL_WINDOW)

    @allure.step("Получить текст заголовка окна подтверждения")
    def get_confirm_text(self):
        return self.find_element(ConfirmOrderLocators.CONFIRM_TEXT).text

    @allure.step("Нажать кнопку 'Да' для подтверждения заказа")
    def click_yes_button(self):
        self.click(ConfirmOrderLocators.YES_BUTTON)
