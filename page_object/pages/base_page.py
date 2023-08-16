from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    USER_NAME = (By.CSS_SELECTOR, "input#user-name")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    LOGIN = (By.CSS_SELECTOR, "input#login-button")
    CART = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def go_to_cart(self):
        self.find(self.CART).click()

    def is_visible(self, locator):
        return self.find(locator).is_displayed

    def enter_username(self, username):
        username_field = self.find(self.USER_NAME)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find(self.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.find(self.LOGIN).click()

    def wait_for_visibility(self, locator):
        return self._wait.until((EC.visibility_of_element_located(locator)))

    def wait_for_disappear(self, locator):
        return self._wait.until_not((EC.presence_of_element_located(locator)))

    def wait_for_invisibility(self, locator):
        return self._wait.until((EC.invisibility_of_element_located(locator)))

    def wait_for_clickable(self, locator):
        return self._wait.until((EC.element_to_be_clickable(locator)))
