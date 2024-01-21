import os

import pytest as pytest
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def user_name():
    return os.getenv("MYUSERNAME")


@pytest.fixture
def password():
    return os.getenv("PASSWORD")


@pytest.fixture(scope="module")
def driver_playground():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def navigate_to_website(driver_playground):
    driver_playground.get("http://uitestingplayground.com/")
    yield driver_playground



