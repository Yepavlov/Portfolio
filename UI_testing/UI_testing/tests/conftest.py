import os

import pytest as pytest
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def username_herokuapp():
    return os.getenv("USERNAME_HEROKUAPP")


@pytest.fixture
def password_herokuapp():
    return os.getenv("PASSWORD_HEROKUAPP")


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def navigate_to_website(driver):
    driver.get("http://the-internet.herokuapp.com/")
    yield driver
