from selenium.webdriver.common.by import By

class SecondOrderPageLocators:
    CALENDAR_BUTTON = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_DATE = (By.XPATH, '//div[contains(@class, "react-datepicker__day") and text()="22"]')
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, '//div[@class="Dropdown-control"]')
    RENTAL_PERIOD_ONE_DAY_OPTION = (By.XPATH, '//div[text()="сутки"]')
    RENTAL_PERIOD_SEVEN_DAYS_OPTION = (By.XPATH, '//div[text()="семеро суток"]')
    COLOUR_BLACK = [By.ID, 'black']
    COLOUR_GREY = [By.ID, 'grey']
    COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[contains(@class, "Button_Button__ra12g") and not(contains(text(), "Назад"))]')
    BACK_BUTTON = (By.XPATH, '//button[text()="Назад"]')
    CONFIRMATION_MODAL = (By.CSS_SELECTOR, 'div.Order_Modal__YZ-d3')
