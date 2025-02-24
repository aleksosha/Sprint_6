from selenium.webdriver.common.by import By

class UpperBasePageLocators:
    UPPER_ORDER_BUTTON = (By.XPATH, './/button[contains(text(), "Заказать")]')
    BIKE_FOR_WHOM = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')  # Проверка на загрузку страницы
