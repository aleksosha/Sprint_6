import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..locators.down_order_button_locators import DownBasePageLocators

class DownOrderButtonPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим страницу до кнопки "Заказать"')
    def scroll_to_order_button(self):
        button = WebDriverWait(self.driver, 15).until(
            ec.presence_of_element_located(DownBasePageLocators.ORDER_BUTTON)
        )

        for _ in range(10):
            self.driver.execute_script('window.scrollBy(0, 100);')
            time.sleep(0.3)

            if button.is_displayed():
                break

        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(button))

    @allure.step('Кликаем по кнопке "Заказать"')
    def click_down_order_button(self):
        self.scroll_to_order_button()
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(DownBasePageLocators.ORDER_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(ec.url_contains('/order'))

    @allure.step('Проверяем, что страница заказа открыта')
    def is_order_page_opened(self):
        try:
            WebDriverWait(self.driver, 15).until(
                ec.presence_of_element_located((By.XPATH, '//div[contains(text(), "Для кого самокат")]'))
            )
            print(f'Текущий URL: {self.driver.current_url}')
            return self.driver.current_url.startswith('https://qa-scooter.praktikum-services.ru/order')
        except Exception as e:
            print(f'Ошибка при проверке открытия страницы: {e}')
            return False