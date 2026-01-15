from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import (
    FAQ_BLOCK,
    FAQ_QUESTIONS,
    FAQ_ANSWERS,
    ORDER_BUTTON_TOP,
    ORDER_BUTTON_BOTTOM
)
from config.urls import BASE_URL


class MainPage(BasePage):
    url = BASE_URL

    def open(self):
        super().open(self.url)

    def scroll_to_faq(self):
        self.scroll_into_view(FAQ_BLOCK)

    def click_faq_question(self, index):
        questions = self.wait_presence_all(FAQ_QUESTIONS)
        self.click(questions[index])

    def get_faq_answer_text(self, index):
        answers = self.wait_presence_all(FAQ_ANSWERS)
        answer = answers[index]
        self.wait.until(EC.visibility_of(answer))
        return answer.text

    def click_order_top(self):
        self.click(ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.scroll_into_view(ORDER_BUTTON_BOTTOM)
        self.click(ORDER_BUTTON_BOTTOM)

    def is_main_page_opened(self):
        return self.wait_url_to_be(self.url)
