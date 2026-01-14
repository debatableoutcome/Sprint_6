import pytest
import allure

from pages.main_page import MainPage
from data.faq_data import FAQ_DATA


class TestFaq:
    @allure.title('Отображение ответа в блоке FAQ')
    @allure.description('Проверка, что при клике на вопрос открывается корректный ответ')
    @pytest.mark.parametrize(
        'index, expected_answer',
        [(index, data['answer']) for index, data in FAQ_DATA.items()],
        ids=[f'faq_{i}' for i in FAQ_DATA.keys()]
    )
    def test_faq_answer_opens(self, driver, index, expected_answer):
        main_page = MainPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()

        with allure.step('Прокрутить до блока FAQ'):
            main_page.scroll_to_faq()

        with allure.step(f'Клик по вопросу FAQ №{index}'):
            main_page.click_faq_question(index)

        with allure.step('Проверить текст ответа'):
            assert main_page.get_faq_answer_text(index) == expected_answer
