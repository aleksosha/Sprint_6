from selenium.webdriver.common.by import By

class DownBasePageLocators:

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")

    STATUS_ELEMENT = (By.XPATH, "//div[contains(text(), 'Когда аренда заканчивается')]")

    BIKE_FOR_WHOM = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
