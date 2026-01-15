from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_url_to_be(self, url, timeout=None):
        return self.get_wait(timeout).until(EC.url_to_be(url))

    def wait_url_contains(self, text, timeout=None):
        return self.get_wait(timeout).until(EC.url_contains(text))

    def wait_visible(self, locator, timeout=None):
        return self.get_wait(timeout).until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, target, timeout=None):
        return self.get_wait(timeout).until(EC.element_to_be_clickable(target))

    def wait_presence(self, locator, timeout=None):
        return self.get_wait(timeout).until(EC.presence_of_element_located(locator))

    def wait_presence_all(self, locator, timeout=None):
        return self.get_wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, target, timeout=None):
        element = self.wait_clickable(target, timeout=timeout)
        element.click()
        return element

    def type(self, locator, text, timeout=None):
        element = self.wait_visible(locator, timeout=timeout)
        element.clear()
        element.send_keys(text)
        return element


    def scroll_into_view(self, locator, timeout=None):
        element = self.wait_presence(locator, timeout=timeout)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
        return element

    def switch_to_new_tab(self, timeout=None):
        current_window = self.driver.current_window_handle
        self.get_wait(timeout).until(EC.number_of_windows_to_be(2))

        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break

    def get_wait(self, timeout):
        return WebDriverWait(self.driver, timeout if timeout is not None else self.timeout)

