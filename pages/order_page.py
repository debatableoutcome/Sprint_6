from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import (
    INPUT_FIRST_NAME, INPUT_LAST_NAME, INPUT_ADDRESS,
    INPUT_METRO, METRO_DROPDOWN, METRO_OPTIONS, INPUT_PHONE,
    BUTTON_NEXT,
    INPUT_DATE, CALENDAR_DAY,
    DROPDOWN_RENT, DROPDOWN_OPTIONS,
    CHECKBOX_BLACK, CHECKBOX_GREY,
    INPUT_COMMENT, BUTTON_ORDER, MODAL_SUCCESS_TITLE,
    BUTTON_CONFIRM_YES, MODAL_CONFIRM_TITLE,
    SCOOTER_LOGO, YANDEX_LOGO
)


class OrderPage(BasePage):
    def fill_step_one(self, data):
        self.type(INPUT_FIRST_NAME, data['first_name'])
        self.type(INPUT_LAST_NAME, data['last_name'])
        self.type(INPUT_ADDRESS, data['address'])

        self.choose_metro(data['metro'])
        self.type(INPUT_PHONE, data['phone'])

    def choose_metro(self, metro_text):
        metro_input = self.wait_clickable(INPUT_METRO)
        metro_input.click()

        metro_input.send_keys(Keys.CONTROL, 'a')
        metro_input.send_keys(Keys.BACKSPACE)
        metro_input.send_keys(metro_text)

        self.wait_visible(METRO_DROPDOWN)
        options = self.wait_presence_all(METRO_OPTIONS)
        options[0].click()

    def click_next(self):
        self.click(BUTTON_NEXT)

    def fill_step_two(self, data):
        self.click(INPUT_DATE)
        self.click(CALENDAR_DAY)

        self.click(DROPDOWN_RENT)
        options = self.wait_presence_all(DROPDOWN_OPTIONS)

        for option in options:
            if option.text.strip() == data['rent_period'].strip():
                option.click()
                break

        if data['color'] == 'black':
            self.click(CHECKBOX_BLACK)
        else:
            self.click(CHECKBOX_GREY)

        self.type(INPUT_COMMENT, data['comment'])

    def submit_order(self):
        self.click(BUTTON_ORDER)

        self.wait_visible(MODAL_CONFIRM_TITLE)
        self.click(BUTTON_CONFIRM_YES)

        return self.wait_visible(MODAL_SUCCESS_TITLE)

    def click_scooter_logo(self):
        self.click(SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(YANDEX_LOGO)

    def switch_to_dzen_tab(self):
        self.switch_to_new_tab(timeout=20)
        self.wait_url_contains('dzen.ru', timeout=30)
