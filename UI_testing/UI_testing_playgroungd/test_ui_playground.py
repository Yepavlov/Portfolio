from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip


def test_chrome_cpu(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/dynamictable'").click()
    cell_cpu = navigate_to_website.find_element(
        By.XPATH,
        "//span[contains(text(), 'Chrome')]/following-sibling::span[contains(text(), '%')][1]",
    )
    field_chrome_cpu = navigate_to_website.find_element(By.CSS_SELECTOR, "p.bg-warning")
    assert cell_cpu.text == field_chrome_cpu.text.replace("Chrome CPU: ", "")


def test_client_side_delay(navigate_to_website, driver_playground):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/clientdelay'").click()
    navigate_to_website.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    wait = WebDriverWait(driver_playground, 20)
    appeared_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )
    assert appeared_field.text == "Data calculated on the client side."


def test_load_delay(navigate_to_website, driver_playground):
    wait = WebDriverWait(driver_playground, 20)
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/loaddelay'").click()
    appeared_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    assert appeared_button


def test_text_input(navigate_to_website):
    wait = WebDriverWait(navigate_to_website, 15)
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/textinput']").click()
    navigate_to_website.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(
        "Hello World"
    )
    navigate_to_website.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    button_element = navigate_to_website.find_element(
        By.CSS_SELECTOR, "button.btn.btn-primary"
    )
    assert button_element.text == "Hello World"


def test_scrollbars(navigate_to_website):
    wait = WebDriverWait(navigate_to_website, 15)
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/scrollbars']").click()
    action = ActionChains(navigate_to_website)
    for _ in range(5):
        action.send_keys(Keys.ARROW_RIGHT).perform()
    for _ in range(3):
        action.send_keys(Keys.ARROW_DOWN).perform()
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    ).click()


def test_sampleapp(navigate_to_website, user_name, password):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/sampleapp']").click()
    field_user = navigate_to_website.find_element(
        By.CSS_SELECTOR, "input[name='UserName']"
    )
    field_user.clear()
    field_user.send_keys(user_name)
    field_password = navigate_to_website.find_element(
        By.CSS_SELECTOR, "input[name='Password']"
    )
    field_password.clear()
    field_password.send_keys(password)
    navigate_to_website.find_element(By.CSS_SELECTOR, "button#login").click()
    field_login_status = navigate_to_website.find_element(
        By.CSS_SELECTOR, "label#loginstatus"
    )
    assert f"Welcome, {user_name}!" == field_login_status.text


def test_mouse_over(navigate_to_website):
    wait = WebDriverWait(navigate_to_website, 15)
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/mouseover']").click()
    button_click_me = navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[title='Click me']"
    )
    action = ActionChains(navigate_to_website)
    action.move_to_element(button_click_me).perform()
    button_click_me_real = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='Active Link']"))
    )
    for _ in range(5):
        button_click_me_real.click()
    counter = navigate_to_website.find_element(By.CSS_SELECTOR, "span#clickCount")
    assert "5" == counter.text


def test_shadow_dom(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/shadowdom']").click()
    shadow_root = navigate_to_website.find_element(
        By.CSS_SELECTOR, "div > guid-generator"
    ).shadow_root
    shadow_root.find_element(By.CSS_SELECTOR, "button.button-generate").click()
    shadow_root.find_element(By.CSS_SELECTOR, "button.button-copy").click()
    clipboard_value = pyperclip.paste()
    shadow_text = shadow_root.find_element(By.CSS_SELECTOR, "input.edit-field")
    shadow_text.send_keys(Keys.CONTROL + "a")
    shadow_text.send_keys(Keys.CONTROL + "c")
    generated_text = pyperclip.paste()
    assert clipboard_value == generated_text
