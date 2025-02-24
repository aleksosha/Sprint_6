import allure
import pytest
from ..pages.down_order_button import DownOrderButtonPage


@pytest.mark.usefixtures('driver')
class TestDownOrderButton:

    @allure.step("Тест: Нажимаем на кнопку 'Заказать' и проверяем, что страница откроется")
    def test_open_order_page_from_down_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        page = DownOrderButtonPage(driver)
        page.click_down_order_button()

        assert page.is_order_page_opened()

