from selenium.webdriver.common.by import By
from ..data.faq_data import QUESTIONS  # Импортируем вопросы

class FAQPageLocators:
    FAQ_SECTION = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")

    QUESTION_TEMPLATE = "//div[contains(@id, 'accordion__heading') and contains(text(), '{}')]"
    ANSWER_TEMPLATE = "//div[contains(@id, 'accordion__panel') and not(@hidden)]//p"

    # Теперь QUESTIONS импортируются из faq_data
    QUESTIONS = QUESTIONS

