import allure
import pytest
from ..pages.down_order_button import DownOrderButtonPage


@pytest.mark.usefixtures('driver')
class TestDownOrderButton:

    @allure.title("Тест: Нажимаем на кнопку 'Заказать' и проверяем, что страница откроется")
    def test_open_order_page_from_down_button(self, driver):
        page = DownOrderButtonPage(driver)
        page.open_main_page()
        page.click_down_order_button()

        page.wait_for_url_contains("order")
        assert "order" in page.get_current_url()
