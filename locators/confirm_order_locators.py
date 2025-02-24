from selenium.webdriver.common.by import By

class ConfirmOrderLocators:
    MODAL_WINDOW = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    CONFIRM_TEXT = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
