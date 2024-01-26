from page_object_training.pages.login_page import LoginPage
from page_object_training.pages.product_page import ProductsPage


def test_login_with_valid_data(driver, username_saucedemo, password_saucedemo):
    login_page = LoginPage(driver)
    login_page.enter_username(username_saucedemo)
    login_page.enter_password(password_saucedemo)
    login_page.click_login()
    product_page = ProductsPage(driver)
    product_page.is_url_matches()


def test_login_without_username(driver, password_saucedemo):
    login_page = LoginPage(driver)
    login_page.enter_password(password_saucedemo)
    login_page.click_login()
    login_page.verify_login_without_or_invalid_username()


def test_login_without_username_and_password(driver):
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.verify_login_without_or_invalid_username()


def test_login_with_invalid_username(driver, password_saucedemo):
    login_page = LoginPage(driver)
    login_page.enter_username("Invalid_username")
    login_page.enter_password(password_saucedemo)
    login_page.click_login()
    login_page.verify_login_with_invalid_data()


def test_login_with_invalid_password(driver, username_saucedemo):
    login_page = LoginPage(driver)
    login_page.enter_username(username_saucedemo)
    login_page.enter_password("Invalid_password")
    login_page.click_login()
    login_page.verify_login_with_invalid_data()


def test_login_without_password(driver, username_saucedemo):
    login_page = LoginPage(driver)
    login_page.enter_username(username_saucedemo)
    login_page.click_login()
    login_page.verify_login_without_password()


def test_login_blocked_user(driver, password_saucedemo):
    login_page = LoginPage(driver)
    login_page.enter_username("locked_out_user")
    login_page.enter_password(password_saucedemo)
    login_page.click_login()
    login_page.verify_login_blocked_user()
