import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.faq_locators import FAQPageLocators

class FAQPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Скроллим до секции 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        section = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(FAQPageLocators.FAQ_SECTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", section)
        time.sleep(1)  # Ждём прогрузки

    @allure.step("Кликаем на вопрос '{question}'")
    def click_question(self, question):
        question_locator = (By.XPATH, FAQPageLocators.QUESTION_TEMPLATE.format(question))
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(question_locator)
        ).click()

        time.sleep(1)

    @allure.step("Проверяем, что ответ на вопрос '{question}' отображается")
    def is_answer_visible(self, question, expected_answer):
        """Ожидание и проверка ответа"""
        answer_locator = (By.XPATH, FAQPageLocators.ANSWER_TEMPLATE)

        try:
            answer_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(answer_locator)
            )
            actual_answer = answer_element.text.strip()
            print(f"Ожидаемый ответ: {expected_answer}")
            print(f"Фактический ответ: {actual_answer}")
            return actual_answer == expected_answer
        except:
            return False
