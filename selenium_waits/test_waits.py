from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alert_wait(navigate_to_url, driver):
    wait = WebDriverWait(driver, 10)
    navigate_to_url.find_element(By.CSS_SELECTOR, "button#alert").click()
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "I got opened after 5 secods" in alert.text
    alert.accept()


def test_change_text_to_selenium(navigate_to_url, driver):
    wait = WebDriverWait(driver, 20)
    navigate_to_url.find_element(By.CSS_SELECTOR, "button#populate-text").click()
    target_element = driver.find_element(By.CSS_SELECTOR, "h2#h2")
    expected_text = "Selenium Webdriver"
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h2#h2"), expected_text)
    )
    assert expected_text in target_element.text


def test_display_button(navigate_to_url, driver):
    wait = WebDriverWait(driver, 20)
    navigate_to_url.find_element(By.CSS_SELECTOR, "button#display-other-button").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#hidden")))
    element = driver.find_element(By.CSS_SELECTOR, "button#hidden")
    assert element.is_displayed()


def test_enable_button(navigate_to_url, driver):
    wait = WebDriverWait(driver, 20)
    navigate_to_url.find_element(By.CSS_SELECTOR, "button#enable-button").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#disable")))
    element = driver.find_element(By.CSS_SELECTOR, "button#disable")
    assert element.is_enabled()


def test_button_checkbox(navigate_to_url, driver):
    wait = WebDriverWait(driver, 20)
    navigate_to_url.find_element(By.CSS_SELECTOR, "button#checkbox").click()
    wait.until(EC.element_located_to_be_selected((By.CSS_SELECTOR, "input#ch")))
    checkbox = driver.find_element(By.CSS_SELECTOR, "input#ch")
    assert checkbox.is_selected()
