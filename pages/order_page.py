from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


from locators.order_page_locators import (
    INPUT_FIRST_NAME, INPUT_LAST_NAME, INPUT_ADDRESS,
    INPUT_METRO, METRO_DROPDOWN, METRO_OPTIONS, INPUT_PHONE,
    BUTTON_NEXT,
    INPUT_DATE, CALENDAR_DAY,
    DROPDOWN_RENT, DROPDOWN_OPTIONS,
    CHECKBOX_BLACK, CHECKBOX_GREY,
    INPUT_COMMENT, BUTTON_ORDER, MODAL_SUCCESS_TITLE,
    BUTTON_CONFIRM_YES, MODAL_CONFIRM_TITLE, SCOOTER_LOGO, YANDEX_LOGO
)


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_step_one(self, data):
        self.wait.until(EC.visibility_of_element_located(INPUT_FIRST_NAME)).send_keys(data['first_name'])
        self.driver.find_element(*INPUT_LAST_NAME).send_keys(data['last_name'])
        self.driver.find_element(*INPUT_ADDRESS).send_keys(data['address'])

        self.choose_metro(data['metro'])
        self.wait.until(EC.element_to_be_clickable(INPUT_PHONE)).send_keys(data['phone'])

    def choose_metro(self, metro_text):
        metro_input = self.wait.until(EC.element_to_be_clickable(INPUT_METRO))
        metro_input.click()

        metro_input.send_keys(Keys.CONTROL, 'a')
        metro_input.send_keys(Keys.BACKSPACE)

        metro_input.send_keys(metro_text)

        self.wait.until(EC.visibility_of_element_located(METRO_DROPDOWN))
        self.wait.until(EC.presence_of_all_elements_located(METRO_OPTIONS))

        options = self.driver.find_elements(*METRO_OPTIONS)
        options[0].click()

    def click_next(self):
        self.wait.until(EC.element_to_be_clickable(BUTTON_NEXT)).click()

    def fill_step_two(self, data):
        self.wait.until(EC.element_to_be_clickable(INPUT_DATE)).click()
        self.wait.until(EC.element_to_be_clickable(CALENDAR_DAY)).click()

        self.wait.until(EC.element_to_be_clickable(DROPDOWN_RENT)).click()
        for option in self.wait.until(EC.presence_of_all_elements_located(DROPDOWN_OPTIONS)):
            if option.text.strip() == data['rent_period'].strip():
                option.click()
                break

        color_checkbox = {
            'black': CHECKBOX_BLACK,
            'grey': CHECKBOX_GREY,
        }[data['color']]

        self.driver.find_element(*color_checkbox).click()

        self.driver.find_element(*INPUT_COMMENT).send_keys(data['comment'])

    def submit_order(self):
        self.wait.until(EC.element_to_be_clickable(BUTTON_ORDER)).click()

        self.wait.until(EC.visibility_of_element_located(MODAL_CONFIRM_TITLE))
        self.wait.until(EC.element_to_be_clickable(BUTTON_CONFIRM_YES)).click()

        return self.wait.until(EC.visibility_of_element_located(MODAL_SUCCESS_TITLE))
    
    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(SCOOTER_LOGO)).click()

    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(YANDEX_LOGO)).click()

    def switch_to_dzen_tab(self):
        WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

        WebDriverWait(self.driver, 30).until(EC.url_contains('dzen.ru'))




