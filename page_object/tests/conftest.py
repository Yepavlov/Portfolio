import pytest as pytest
from selenium import webdriver

from pages.base_page import BasePage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def username():
    return "standard_user"


@pytest.fixture(scope="session")
def password():
    return "secret_sauce"


@pytest.fixture()
def logged_in_main_page(driver, username, password):
    main_page = LoginPage(driver)
    main_page.enter_username(username)
    main_page.enter_password(password)
    main_page.click_login_button()
    return main_page
