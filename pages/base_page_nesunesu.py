from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePagesNN:

    def __init__(self, driver):
        self.driver = driver

    def click_method(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_method(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def get_url(self):
        get_url = self.driver.current_url
        return get_url

    def expectation(self, locator):
        return WebDriverWait(self.driver, 25).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 25).until(
            expected_conditions.element_to_be_clickable(locator))
