from selenium.webdriver.common.by import By


FAQ_BLOCK = (
    By.CLASS_NAME,
    'accordion'
)

FAQ_QUESTIONS = (
    By.CSS_SELECTOR,
    '[data-accordion-component=\'AccordionItem\'] .accordion__button'
)

FAQ_ANSWERS = (
    By.CSS_SELECTOR,
    '[data-accordion-component=\'AccordionItemPanel\']'
)

ORDER_BUTTON_TOP = (By.XPATH, '(//button[normalize-space()=\'Заказать\'])[1]')
ORDER_BUTTON_BOTTOM = (By.XPATH, '(//button[normalize-space()=\'Заказать\'])[2]')

SCOOTER_LOGO = (By.XPATH, '//a[contains(@class, \'Header_Logo\')]')
YANDEX_LOGO = (By.XPATH, '//a[contains(@class, \'Header_LogoYandex\') or contains(@href, \'yandex\')]')