from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    USER_NAME = (By.CSS_SELECTOR, "input#user-name")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    LOGIN = (By.CSS_SELECTOR, "input#login-button")
    CART = (By.CSS_SELECTOR, "a.shopping_cart_link")
    DIV_USER_AND_PASSWORD_DNT_MATCH = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: "
        "Username and password do not match any user in this service')]",
    )
    DIV_LOCKED_USER = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: Sorry, this user has been locked out.')]",
    )
    DIV_USERNAME_IS_REQUIRED = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: Username is required')]",
    )
    DIV_PASSWORD_IS_REQUIRED = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: Password is required')]",
    )

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

    def verify_login_with_incorrect_username(self):
        div_error = self.find(self.DIV_USER_AND_PASSWORD_DNT_MATCH)
        assert (
            "Epic sadface: Username and password do not match any user in this service"
            in div_error.text
        )

    def verify_locked_user(self):
        div_error = self.find(self.DIV_LOCKED_USER)
        assert "Epic sadface: Sorry, this user has been locked out." in div_error.text

    def verify_login_without_username(self):
        div_error = self.find(self.DIV_USERNAME_IS_REQUIRED)
        assert "Epic sadface: Username is required" in div_error.text

    def verify_password_without_username(self):
        div_error = self.find(self.DIV_PASSWORD_IS_REQUIRED)
        assert "Epic sadface: Password is required" in div_error.text
