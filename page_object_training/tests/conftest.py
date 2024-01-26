import pytest as pytest
from selenium import webdriver
import os
from dotenv import load_dotenv

from page_object_training.pages.login_page import LoginPage

load_dotenv()


@pytest.fixture
def driver():
    driver_chrome = webdriver.Chrome()
    driver_chrome.maximize_window()
    driver_chrome.get("https://www.saucedemo.com/")
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture
def username_saucedemo():
    return os.getenv("USERNAME_SAUCEDEMO")


@pytest.fixture
def password_saucedemo():
    return os.getenv("PASSWORD_SAUCEDEMO")


@pytest.fixture
def logged_in_user(driver, username_saucedemo, password_saucedemo):
    login_page = LoginPage(driver)
    login_page.enter_username(username_saucedemo)
    login_page.enter_password(password_saucedemo)
    login_page.click_login()
    return login_page
