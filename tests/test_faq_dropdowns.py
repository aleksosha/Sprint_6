import pytest
import allure
from ..pages.faq_page import FAQPage
from ..locators.faq_locators import FAQPageLocators


@allure.epic("Тесты FAQ")
@pytest.mark.usefixtures("driver")
class TestFAQDropdowns:

    @allure.story("Проверка раскрытия вопросов и отображения ответов")
    @pytest.mark.parametrize("question, expected_answer", FAQPageLocators.QUESTIONS.items())
    def test_faq_dropdown(self, driver, question, expected_answer):
        driver.get("https://qa-scooter.praktikum-services.ru/")

        faq_page = FAQPage(driver)
        faq_page.scroll_to_faq_section()
        faq_page.click_question(question)

        print(f"Проверяем ответ для вопроса: {question}")
        assert faq_page.is_answer_visible(question, expected_answer)
