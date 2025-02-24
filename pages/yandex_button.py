import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..locators.yandex_button_locators import YandexButtonLocators

class YandexButton:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликаем")
    def click_yandex_button(self):
        WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable(YandexButtonLocators.YANDEX_BUTTON)
).click()