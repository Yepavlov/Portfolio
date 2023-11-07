from pages.login_page import LoginPage
from pages.products_page import Products


def test_login(driver, username, password):
    main_page = LoginPage(driver)
    main_page.enter_username(username)
    main_page.enter_password(password)
    main_page.click_login_button()
    product_page = Products(driver)
    assert product_page.is_url_matches()


def test_login_with_incorrect_username(driver, password):
    main_page = LoginPage(driver)
    main_page.enter_username("incorrect_username")
    main_page.enter_password(password)
    main_page.click_login_button()
    main_page.verify_login_with_incorrect_username()


def test_login_with_incorrect_password(driver, username):
    main_page = LoginPage(driver)
    main_page.enter_username(username)
    main_page.enter_password("incorrect_password")
    main_page.click_login_button()
    main_page.verify_login_with_incorrect_username()


def test_login_locked_out_user(driver, password):
    main_page = LoginPage(driver)
    main_page.enter_username("locked_out_user")
    main_page.enter_password(password)
    main_page.click_login_button()
    main_page.verify_locked_user()


def test_login_without_username(driver, password):
    main_page = LoginPage(driver)
    main_page.enter_username("")
    main_page.enter_password(password)
    main_page.click_login_button()
    main_page.verify_login_without_username()


def test_login_without_password(driver, username):
    main_page = LoginPage(driver)
    main_page.enter_username(username)
    main_page.enter_password("")
    main_page.click_login_button()
    main_page.verify_password_without_username()
