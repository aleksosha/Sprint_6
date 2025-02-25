from selenium.webdriver.common.by import By

class ConfirmOrderLocators:
    MODAL_WINDOW = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    CONFIRM_TEXT = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and contains(text(), "Хотите оформить заказ?")]')
    YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__") and text()="Да"]')
