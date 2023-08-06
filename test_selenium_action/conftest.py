import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    chrome_driver = webdriver.Chrome()

    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture()
def navigate_to_url(driver):
    driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    yield driver
