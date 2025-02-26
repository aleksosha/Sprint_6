from ..pages.first_order_page import FirstOrderPage
from ..pages.second_order_page_seven_days_grey_pearl import SecondOrderPage

class TestOrderPage:
    def test_fill_in_info(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/order')

        # Создаем объект страницы первого заказа
        first_order_page = FirstOrderPage(driver)
        first_order_page.set_name('Александра')
        first_order_page.set_last_name('Дроботун')
        first_order_page.set_address('Фортунатовская 8')
        first_order_page.choose_metro_station()
        first_order_page.set_phone_number('+79169735250')
        first_order_page.click_next_button()

        # Создаем объект страницы второго заказа
        second_order_page = SecondOrderPage(driver)
        second_order_page.click_calendar()
        second_order_page.set_date()
        second_order_page.set_rental_period()
        second_order_page.set_gray_colour()
        second_order_page.set_comment_for_courier("Позвоните за 10 минут до доставки")

        # Кликаем по кнопке "Заказать"
        second_order_page.click_order_button()

        # Проверяем, что модальное окно подтверждения заказа отображается
        assert second_order_page.is_order_confirmed()
