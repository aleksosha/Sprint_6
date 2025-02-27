import allure
from selenium.webdriver.common.by import By
from ..locators.faq_locators import FAQPageLocators
from ..pages.base_page import BasePage

class FAQPage(BasePage):
    @allure.step("Скроллим до секции 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        self.wait_for_element(FAQPageLocators.FAQ_SECTION, timeout=15)
        self.scroll_to_element(FAQPageLocators.FAQ_SECTION)

    @allure.step("Кликаем на вопрос '{question}'")
    def click_question(self, question):
        question_locator = (By.XPATH, FAQPageLocators.QUESTION_TEMPLATE.format(question))
        self.wait_for_element_to_be_clickable(question_locator, timeout=15)
        self.click(question_locator)

    @allure.step("Проверяем, что ответ на вопрос '{question}' отображается")
    def is_answer_visible(self, question, expected_answer):
        answer_locator = (By.XPATH, FAQPageLocators.ANSWER_TEMPLATE)

        try:
            self.wait_for_element(answer_locator, timeout=15)
            actual_answer = self.find_element(answer_locator).text.strip()
            return actual_answer == expected_answer
        except Exception:
            return False
