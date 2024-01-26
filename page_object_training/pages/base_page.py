from typing import List

from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object_training.pages.locators import CommonLocators


class BasePage(CommonLocators):

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)

    def find_el(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_all_els(self, locator) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    def click_logout(self):
        self.find_el(self.BURGER_MENU_BTN).click()
        self.find_el(self.LOGOUT_BTN).click()

    def click_go_to_cart(self):
        self.find_el(self.CART).click()

    def is_visible(self, locator) -> bool:
        return self.find_el(locator).is_displayed()

    def wait_for_visibility(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def wait_for_present(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        return self._wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_disappear(self, locator):
        try:
            self.wait_for_invisibility(locator)
        except TimeoutException:
            print(f"Element {locator} is still visible")

    def check_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url} does not match Actual URL: {current_url}"
