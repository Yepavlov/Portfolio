import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def navigate_to_url(driver):
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
    return driver
