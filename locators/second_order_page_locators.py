from selenium.webdriver.common.by import By

class SecondOrderPageLocators:
    CALENDAR_BUTTON = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_DATE = (By.XPATH, '//div[contains(@class, "react-datepicker__day") and text()="22"]')
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, '//div[@class="Dropdown-control"]')
    RENTAL_PERIOD_ONE_DAY_OPTION = (By.XPATH, '//div[text()="сутки"]')
    RENTAL_PERIOD_SEVEN_DAYS_OPTION = (By.XPATH, '//div[text()="семеро суток"]')
    BLACK_PEARL = (By.XPATH, '//label[text()="чёрный жемчуг"]')
    GRAY_HOPELESSNESS = (By.XPATH, '//label[text()="серая безысходность"]')
    COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')
    BACK_BUTTON = (By.XPATH, '//button[text()="Назад"]')
