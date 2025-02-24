from selenium.webdriver.common.by import By

class FirstOrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION_CHOICE = (By.XPATH, '//div[text()="Бульвар Рокоссовского"]')
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_PAGE_BUTTON = (By.XPATH, '//button[text()="Далее"]')
