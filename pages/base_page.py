from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_element_displayed(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except Exception:
            return False

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def wait_for_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_for_elements(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_all_elements_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, url_substring, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.url_contains(url_substring)
        )

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.url_to_be(expected_url))
        actual_url = self.driver.current_url
        return actual_url

    def get_current_url(self):
        return self.driver.current_url
