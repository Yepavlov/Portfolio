from selenium.webdriver.common.by import By
from page_object.pages.base_page import BasePage
from page_object.pages.products_page import Products


def test_login(driver, username, password):
    main_page = BasePage(driver)
    main_page.enter_username(username)
    main_page.enter_password(password)
    main_page.click_login_button()
    product_page = Products(driver)
    assert product_page.is_url_matches()


def test_login_with_incorrect_username(driver, password):
    main_page = BasePage(driver)
    main_page.enter_username("incorrect_username")
    main_page.enter_password(password)
    main_page.click_login_button()
    div_error = driver.find_element(
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: "
        "Username and password do not match any user in this service')]",
    )
    assert (
        "Epic sadface: Username and password "
        "do not match any user in this service" in div_error.text
    )


def test_login_with_incorrect_password(driver, username):
    main_page = BasePage(driver)
    main_page.enter_username(username)
    main_page.enter_password("incorrect_password")
    main_page.click_login_button()
    div_error = driver.find_element(
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: "
        "Username and password do not match any user in this service')]",
    )
    assert (
        "Epic sadface: Username and password "
        "do not match any user in this service" in div_error.text
    )


def test_login_locked_out_user(driver, password):
    main_page = BasePage(driver)
    main_page.enter_username("locked_out_user")
    main_page.enter_password(password)
    main_page.click_login_button()
    div_error = driver.find_element(
        By.XPATH,
        "//*[contains(text(), "
        "'Epic sadface: Sorry, this user has been locked out.')]",
    )
    assert "Epic sadface: Sorry, this user has been locked out." in div_error.text


def test_login_without_username(driver, password):
    main_page = BasePage(driver)
    main_page.enter_username("")
    main_page.enter_password(password)
    main_page.click_login_button()
    div_error = driver.find_element(
        By.XPATH, "//*[contains(text(), 'Epic sadface: Username is required')]"
    )
    assert "Epic sadface: Username is required" in div_error.text


def test_login_without_password(driver, username):
    main_page = BasePage(driver)
    main_page.enter_username(username)
    main_page.enter_password("")
    main_page.click_login_button()
    div_error = driver.find_element(
        By.XPATH, "//*[contains(text(), 'Epic sadface: Password is required')]"
    )
    assert "Epic sadface: Password is required" in div_error.text
