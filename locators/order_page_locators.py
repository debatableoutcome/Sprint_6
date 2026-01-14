from selenium.webdriver.common.by import By


INPUT_FIRST_NAME = (By.XPATH, '//input[@placeholder=\'* Имя\']')
INPUT_LAST_NAME = (By.XPATH, '//input[@placeholder=\'* Фамилия\']')
INPUT_ADDRESS = (By.XPATH, '//input[@placeholder=\'* Адрес: куда привезти заказ\']')


INPUT_METRO = (By.CSS_SELECTOR, 'input.select-search__input')
METRO_DROPDOWN = (By.CSS_SELECTOR, 'ul.select-search__options')
METRO_OPTIONS = (By.CSS_SELECTOR, 'ul.select-search__options button.select-search__option')




INPUT_PHONE = (By.XPATH, '//input[@placeholder=\'* Телефон: на него позвонит курьер\']')

BUTTON_NEXT = (By.XPATH, '//button[normalize-space()=\'Далее\']')


INPUT_DATE = (By.XPATH, '//input[@placeholder=\'* Когда привезти самокат\']')
CALENDAR_DAY = (By.CSS_SELECTOR, '.react-datepicker__day:not(.react-datepicker__day--disabled)')
DROPDOWN_RENT = (By.XPATH, '//div[contains(@class, \'Dropdown-control\')]')
DROPDOWN_OPTIONS = (By.XPATH, '//div[contains(@class, \'Dropdown-menu\')]//div[contains(@class, \'Dropdown-option\')]')

CHECKBOX_BLACK = (By.ID, 'black')
CHECKBOX_GREY = (By.ID, 'grey')

INPUT_COMMENT = (By.XPATH, '//input[@placeholder=\'Комментарий для курьера\']')

BUTTON_ORDER = (
    By.XPATH,
    '//div[contains(@class,"Order_Buttons")]//button[normalize-space()="Заказать"]'
)


MODAL = (By.XPATH, '//div[contains(@class,\'Order_Modal\')]')

MODAL_CONFIRM_TITLE = (
    By.XPATH,
    '//div[contains(@class,\'Order_ModalHeader\') and contains(normalize-space(.),\'Хотите оформить заказ\')]'
)

BUTTON_CONFIRM_YES = (
    By.XPATH,
    '//div[contains(@class,\'Order_Modal\')]//button[normalize-space()=\'Да\']'
)

BUTTON_CONFIRM_NO = (
    By.XPATH,
    '//div[contains(@class,\'Order_Modal\')]//button[normalize-space()=\'Нет\']'
)

MODAL_SUCCESS_TITLE = (
    By.XPATH,
    '//div[contains(@class,\'Order_ModalHeader\') and contains(normalize-space(.),\'Заказ оформлен\')]'
)

SCOOTER_LOGO = (By.CSS_SELECTOR, 'a[class^="Header_LogoScooter"]')

YANDEX_LOGO = (By.CSS_SELECTOR, 'a[class^="Header_LogoYandex"]')

