import allure
import pytest
from ..pages.upper_order_button import UpperOrderButtonPage

@pytest.mark.usefixtures("driver")
class TestUpperOrderButton:
    @allure.title("Тест: Нажимаем на кнопку 'Заказать' и проверяем, что страница откроется")
    def test_open_order_page_from_upper_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        page = UpperOrderButtonPage(driver)
        page.click_upper_order_button()
        assert page.is_order_page_opened()