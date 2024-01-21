
from page_object.pages.base_page import BasePage
from page_object.pages.Locators import LocatorsLoginPage


class LoginPage(BasePage, LocatorsLoginPage):

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
