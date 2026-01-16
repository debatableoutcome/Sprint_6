import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA


class TestOrderPage:

    @allure.title('Заказ самоката через кнопку «Заказать» вверху страницы')
    @allure.description('Проверка позитивного сценария оформления заказа с первым набором данных')
    def test_order_from_top_button_shows_success_modal(self, driver):
        """
        Проверяет позитивный сценарий заказа с набором данных 1,
        вход в заказ — кнопка «Заказать» вверху страницы
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()

        with allure.step('Нажать кнопку «Заказать» вверху страницы'):
            main_page.click_order_top()

        with allure.step('Заполнить первый шаг формы заказа'):
            order_page.fill_step_one(ORDER_DATA[0])
            order_page.click_next()

        with allure.step('Заполнить второй шаг формы заказа'):
            order_page.fill_step_two(ORDER_DATA[0])

        with allure.step('Подтвердить заказ и проверить успешное оформление'):
            assert order_page.submit_order()

    @allure.title('Заказ самоката через кнопку «Заказать» внизу страницы')
    @allure.description('Проверка позитивного сценария оформления заказа со вторым набором данных')
    def test_order_from_bottom_button_shows_success_modal(self, driver):
        """
        Проверяет позитивный сценарий заказа с набором данных 2,
        вход в заказ — кнопка «Заказать» внизу страницы
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step('Открыть главную страницу'):
            main_page.open()

        with allure.step('Нажать кнопку «Заказать» внизу страницы'):
            main_page.click_order_bottom()

        with allure.step('Заполнить первый шаг формы заказа'):
            order_page.fill_step_one(ORDER_DATA[1])
            order_page.click_next()

        with allure.step('Заполнить второй шаг формы заказа'):
            order_page.fill_step_two(ORDER_DATA[1])

        with allure.step('Подтвердить заказ и проверить успешное оформление'):
            assert order_page.submit_order()

    @allure.title('Переход на главную по логотипу «Самокат»')
    def test_scooter_logo_redirects_to_main_page(self, driver):
        """
        Проверяет, что кнопка с логотипом «Самокат»
        ведёт на главную страницу со страницы заказа
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_top()

        with allure.step('Клик по логотипу «Самокат»'):
            order_page.click_scooter_logo()

        with allure.step('Проверить, что открылась главная страница'):
            assert main_page.is_main_page_opened()

    @allure.title('Открытие Дзена по логотипу Яндекса в новой вкладке')
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        """
        Проверяет, что кнопка с логотипом Яндекса
        открывает новую вкладку с сайтом dzen.ru
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_top()

        with allure.step('Клик по логотипу Яндекса'):
            order_page.click_yandex_logo()

        with allure.step('Переключиться на новую вкладку и дождаться Дзена'):
            order_page.switch_to_dzen_tab()

        with allure.step('Проверить, что открыт сайт dzen.ru'):
            assert 'dzen.ru' in order_page.get_current_url()

