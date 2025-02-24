import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..locators.confirm_order_locators import ConfirmOrderLocators

class ConfirmOrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание появления окна подтверждения")
    def wait_for_modal(self):
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(ConfirmOrderLocators.MODAL_WINDOW)
        )

    @allure.step("Получить текст заголовка окна подтверждения")
    def get_confirm_text(self):
        return self.driver.find_element(*ConfirmOrderLocators.CONFIRM_TEXT).text

    @allure.step("Нажать кнопку 'Да' для подтверждения заказа")
    def click_yes_button(self):
        self.driver.find_element(*ConfirmOrderLocators.YES_BUTTON).click()
