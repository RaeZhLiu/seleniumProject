from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(3)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_ele(self, wait_condition, time=10):
        return WebDriverWait(self._driver, time).until(wait_condition)