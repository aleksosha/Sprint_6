import allure
from ..pages.yandex_button import YandexButton

class TestUpperOrderButton:
    @allure.title("Тест: Автоматический редирект на Дзен.ру по клику на Яндекс")
    def test_open_order_page_from_upper_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        page = YandexButton(driver)
        page.click_yandex_button()

        expected_url = "https://dzen.ru/?yredirect=true"
        actual_url = page.switch_to_new_window_and_check_url(expected_url)

        assert actual_url == expected_url
