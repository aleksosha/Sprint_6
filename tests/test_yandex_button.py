from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..pages.yandex_button import YandexButton


class TestUpperOrderButton:
    def test_open_order_page_from_upper_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        page = YandexButton(driver)
        page.click_yandex_button()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])

        expected_url = "https://dzen.ru/?yredirect=true"
        WebDriverWait(driver, 10).until(ec.url_to_be(expected_url))
        actual_url = driver.current_url

        assert actual_url == expected_url