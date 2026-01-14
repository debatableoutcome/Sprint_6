from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import (
    FAQ_BLOCK,
    FAQ_QUESTIONS,
    FAQ_ANSWERS,
    ORDER_BUTTON_TOP,
    ORDER_BUTTON_BOTTOM
)
from config.urls import BASE_URL


class MainPage:
    url = BASE_URL

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    def scroll_to_faq(self):
        faq_block = self.wait.until(EC.presence_of_element_located(FAQ_BLOCK))
        self.driver.execute_script('arguments[0].scrollIntoView(true);', faq_block)

    def click_faq_question(self, index):
        questions = self.wait.until(EC.presence_of_all_elements_located(FAQ_QUESTIONS))
        self.wait.until(EC.element_to_be_clickable(questions[index])).click()

    def get_faq_answer_text(self, index):
        answers = self.wait.until(EC.presence_of_all_elements_located(FAQ_ANSWERS))
        answer = answers[index]
        self.wait.until(EC.visibility_of(answer))
        return answer.text

    def click_order_top(self):
        self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON_TOP)).click()

    def click_order_bottom(self):
        btn = self.wait.until(EC.presence_of_element_located(ORDER_BUTTON_BOTTOM))
        self.driver.execute_script('arguments[0].scrollIntoView(true);', btn)
        self.wait.until(EC.element_to_be_clickable(ORDER_BUTTON_BOTTOM)).click()

    def is_main_page_opened(self):
        return self.wait.until(EC.url_to_be(self.url))

