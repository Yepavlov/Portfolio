from page_object_training.pages.base_page import BasePage
from page_object_training.pages.locators import LocatorsLoginPage


class LoginPage(BasePage, LocatorsLoginPage):

    def enter_username(self, username: str):
        field_username = self.find_el(self.USER_NAME)
        field_username.clear()
        field_username.send_keys(username)

    def enter_password(self, password: str):
        field_password = self.find_el(self.PASSWORD)
        field_password.clear()
        field_password.send_keys(password)

    def click_login(self):
        self.find_el(self.LOGIN_BTN).click()

    def verify_login_without_or_invalid_username(self):
        div_error_message = self.find_el(self.DIV_ERROR_MESSAGE)
        assert "Epic sadface: Username is required" == div_error_message.text

    def verify_login_with_invalid_data(self):
        div_error_message = self.find_el(self.DIV_ERROR_MESSAGE)
        assert "Epic sadface: Username and password do not match any user in this service" == div_error_message.text

    def verify_login_without_password(self):
        div_error_message = self.find_el(self.DIV_ERROR_MESSAGE)
        assert "Epic sadface: Password is required" == div_error_message.text

    def verify_login_blocked_user(self):
        div_error_message = self.find_el(self.DIV_ERROR_MESSAGE)
        assert "Epic sadface: Sorry, this user has been locked out." == div_error_message.text
