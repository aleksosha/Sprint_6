from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..locators.upper_order_button_locators import UpperBasePageLocators

class UpperOrderButtonPage:
    def __init__(self, driver):
        self.driver = driver

    def click_upper_order_button(self):
        WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable(UpperBasePageLocators.UPPER_ORDER_BUTTON)
        ).click()

        WebDriverWait(self.driver, 15).until(
            ec.presence_of_element_located(UpperBasePageLocators.BIKE_FOR_WHOM)
        )

        WebDriverWait(self.driver, 15).until(ec.url_contains("/order"))

    def is_order_page_opened(self):
        try:
            WebDriverWait(self.driver, 15).until(
                ec.presence_of_element_located(UpperBasePageLocators.BIKE_FOR_WHOM)
            )
            return self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"
        except:
            return False
