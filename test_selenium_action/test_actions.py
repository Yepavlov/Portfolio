from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dropdown(navigate_to_url, driver):
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/dropdown']").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, "select")
    select = Select(dropdown)
    select.select_by_visible_text("Option 2")
    option2_element = select.first_selected_option
    assert option2_element.text == "Option 2"


def test_checkboxes(navigate_to_url, driver):
    wait = WebDriverWait(driver, 10)
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/checkboxes']").click()
    checkbox1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form :first-child")))
    checkbox1.click()
    checkbox2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form :last-child")))
    checkbox2.click()
    assert checkbox1.is_selected()
    assert not checkbox2.is_selected()


def test_context_menu(navigate_to_url, driver):
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/context_menu']").click()
    box = driver.find_element(By.CSS_SELECTOR, "div #hot-spot")
    action = ActionChains(driver)
    action.context_click(box).perform()
    alert = driver.switch_to.alert
    assert "You selected a context menu" in alert.text


def test_entry_ad(navigate_to_url, driver):
    wait = WebDriverWait(driver, 10)
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/entry_ad']").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal-footer p")))
    driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#restart-ad")))
    driver.find_element(By.CSS_SELECTOR, "a#restart-ad").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
    div = driver.find_element(By.CSS_SELECTOR, "div.modal")
    assert div.is_displayed()


def test_form_authentication(navigate_to_url, driver):
    driver.implicitly_wait(5)
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    driver.find_element(By.CSS_SELECTOR, "input#username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in").click()
    div = driver.find_element(By.CSS_SELECTOR, "h4.subheader")
    assert "Welcome to the Secure Area. When you are done click logout below." in div.text


def test_frames(navigate_to_url, driver):
    driver.implicitly_wait(5)
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/frames']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/iframe']").click()
    driver.switch_to.frame("mce_0_ifr")
    body = driver.find_element(By.CSS_SELECTOR, "#tinymce")
    body.clear()
    body.send_keys("Hello world!")
    assert "Hello world!" in body.text


def test_horizontal_slider(navigate_to_url, driver):
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/horizontal_slider']").click()
    slider = driver.find_element(By.CSS_SELECTOR, "input")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider, 50, 0).perform()
    slider.send_keys(Keys.ARROW_LEFT)
    slider.send_keys(Keys.ARROW_LEFT)
    slider.send_keys(Keys.ARROW_LEFT)
    assert "3" in driver.find_element(By.CSS_SELECTOR, "span#range").text


def test_input(navigate_to_url, driver):
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/inputs']").click()
    input_element = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_element.clear()
    input_element.send_keys("123")
    actual_value = input_element.get_attribute("value")
    assert "123" == actual_value


def test_key_presses(navigate_to_url, driver):
    navigate_to_url.find_element(By.CSS_SELECTOR, "a[href='/key_presses']").click()
    field = driver.find_element(By.CSS_SELECTOR, "input#target")
    field.clear()
    field.send_keys("G")
    assert "You entered: G" in driver.find_element(By.CSS_SELECTOR, "p#result").text
