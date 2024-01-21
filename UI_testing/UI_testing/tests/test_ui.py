from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ab_testing(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/abtest']").click()
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[target='_blank']").click()
    navigate_to_website.switch_to.window(navigate_to_website.window_handles[1])
    searching_field = navigate_to_website.find_element(
        By.XPATH, "//h1[text()='Make sure your code lands']"
    )
    assert "Make sure your code lands" == searching_field.text


def test_add_remove_elements(navigate_to_website):
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/add_remove_elements/']"
    ).click()
    button_add_element = navigate_to_website.find_element(
        By.CSS_SELECTOR, "button[onclick='addElement()']"
    )
    for _ in range(5):
        button_add_element.click()
    buttons_delete = navigate_to_website.find_elements(
        By.XPATH, "//button[text()='Delete']"
    )
    assert len(buttons_delete) == 5
    for button in buttons_delete:
        button.click()
    assert (
        len(navigate_to_website.find_elements(By.XPATH, "//button[text()='Delete']"))
        == 0
    ), "Element button_delete is present on the webpage"


def test_checkboxes(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/checkboxes']").click()
    checkbox_1 = navigate_to_website.find_element(
        By.XPATH, "//input[@type='checkbox'][1]"
    )
    checkbox_1.click()
    checkbox_2 = navigate_to_website.find_element(
        By.XPATH, "//input[@type='checkbox'][2]"
    )
    checkbox_2.click()
    assert checkbox_1.is_selected()
    assert not checkbox_2.is_selected()


def test_context_menu(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/context_menu']").click()
    box = navigate_to_website.find_element(By.CSS_SELECTOR, "div#hot-spot")
    action = ActionChains(navigate_to_website)
    action.context_click(box).perform()
    navigate_to_website.switch_to.alert.accept()
    assert (
        navigate_to_website.find_element(By.XPATH, "//h3").text == "Context Menu"
    ), "The alert is still active"


def test_drag_and_drop(navigate_to_website):
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/drag_and_drop']"
    ).click()
    div_left = navigate_to_website.find_element(By.CSS_SELECTOR, "div#column-a")
    div_right = navigate_to_website.find_element(By.CSS_SELECTOR, "div#column-b")
    action = ActionChains(navigate_to_website)
    action.drag_and_drop(div_left, div_right).perform()
    assert "B" in div_left.text
    assert "A" in div_right.text


def test_dropdown(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/dropdown']").click()
    dropdown = navigate_to_website.find_element(By.CSS_SELECTOR, "select#dropdown")
    select = Select(dropdown)
    select.select_by_value("2")
    assert select.first_selected_option.text == "Option 2"


def test_dynamic_controls(navigate_to_website):
    wait = WebDriverWait(navigate_to_website, 10)
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/dynamic_controls']"
    ).click()
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "button[onclick='swapCheckbox()']"
    ).click()
    try:
        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "input[type='checkbox']")
            )
        )
        assert True, "The element is absent on the page"
    except TimeoutException:
        assert False, "The element is still present on the page"
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "button[onclick='swapInput()']"
    ).click()
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']")))
        assert True, "The field can be filled in"
    except TimeoutException:
        assert False, "The field is not clickable"


def test_dynamic_loading(navigate_to_website):
    wait = WebDriverWait(navigate_to_website, 10)
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/dynamic_loading']"
    ).click()
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/dynamic_loading/1']"
    ).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div > button")))
    navigate_to_website.find_element(By.CSS_SELECTOR, "div > button").click()
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert (
        "Hello World!"
        in navigate_to_website.find_element(
            By.XPATH, "//h4[text()='Hello World!']"
        ).text
    )
    navigate_to_website.back()
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/dynamic_loading/2']"
    ).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div > button")))
    navigate_to_website.find_element(By.CSS_SELECTOR, "div > button").click()
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert (
        "Hello World!"
        in navigate_to_website.find_element(
            By.XPATH, "//h4[text()='Hello World!']"
        ).text
    )


def test_form_authentication_and_logout(
    navigate_to_website, username_herokuapp, password_herokuapp
):
    wait = WebDriverWait(navigate_to_website, 10)
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    navigate_to_website.find_element(By.CSS_SELECTOR, "input#username").send_keys(
        username_herokuapp
    )
    navigate_to_website.find_element(By.CSS_SELECTOR, "input#password").send_keys(
        password_herokuapp
    )
    navigate_to_website.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in").click()
    try:
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "i.icon-2x.icon-signout")
            )
        )
        assert True, "Login was successful"
    except TimeoutException:
        assert False, "Failed to login"
    navigate_to_website.find_element(By.CSS_SELECTOR, "i.icon-2x.icon-signout").click()
    assert (
        navigate_to_website.find_element(By.CSS_SELECTOR, "h2").text == "Login Page"
    ), "Failed to logout"


def test_form_authentication_with_invalid_data(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    navigate_to_website.find_element(By.CSS_SELECTOR, "input#username").send_keys(
        "Invalid_username"
    )
    navigate_to_website.find_element(By.CSS_SELECTOR, "input#password").send_keys(
        "Invalid_password"
    )
    navigate_to_website.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in").click()
    div_inform = navigate_to_website.find_element(By.CSS_SELECTOR, "div.flash.error")
    actual_result = div_inform.text.replace("\n×", "")
    assert actual_result == "Your username is invalid!"


def test_frames(navigate_to_website):
    wait = WebDriverWait(navigate_to_website, 10)
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/frames']").click()
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/iframe']").click()
    iframe = navigate_to_website.find_element(By.CSS_SELECTOR, "iframe#mce_0_ifr")
    navigate_to_website.switch_to.frame(iframe)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body#tinymce")))
    input_field = navigate_to_website.find_element(By.CSS_SELECTOR, "body#tinymce")
    input_field.click()
    input_field.send_keys(Keys.CONTROL + "a")
    input_field.send_keys(Keys.BACKSPACE)
    input_field.send_keys("Hello world!")
    assert input_field.text == "Hello world!"
    input_field.send_keys(Keys.CONTROL + "a")
    navigate_to_website.switch_to.default_content()
    button_italic = navigate_to_website.find_element(
        By.CSS_SELECTOR, "button[title='Italic']"
    )
    button_italic.click()
    assert button_italic.is_enabled(), "Button_italic is enabled"


def test_horizontal_slider(navigate_to_website):
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/horizontal_slider']"
    ).click()
    slider = navigate_to_website.find_element(By.CSS_SELECTOR, "input[type='range']")
    action = ActionChains(navigate_to_website)
    action.drag_and_drop_by_offset(slider, 50, 0).perform()
    for _ in range(3):
        slider.send_keys(Keys.ARROW_LEFT)
    span_range = navigate_to_website.find_element(By.CSS_SELECTOR, "span#range")
    assert "3" == span_range.text


def test_hovers(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/hovers']").click()
    list_images = navigate_to_website.find_elements(
        By.XPATH, "//img[@alt='User Avatar']"
    )
    action = ActionChains(navigate_to_website)
    for index, image in enumerate(list_images, start=1):
        action.move_to_element(image).perform()
        navigate_to_website.find_element(
            By.CSS_SELECTOR, f"a[href='/users/{index}']"
        ).click()
        actual_result = navigate_to_website.find_element(By.CSS_SELECTOR, "h1").text
        assert "Not Found" == actual_result
        navigate_to_website.back()


def test_inputs(navigate_to_website):
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/inputs']").click()
    input_field = navigate_to_website.find_element(
        By.CSS_SELECTOR, "input[type='number']"
    )
    input_field.clear()
    input_field.send_keys("25")
    actual_result = input_field.get_attribute("value")
    assert "25" == actual_result
    for _ in range(25):
        input_field.send_keys(Keys.ARROW_DOWN)
    actual_result = input_field.get_attribute("value")
    assert "0" == actual_result


def test_jquery_ui_menus(navigate_to_website):
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/jqueryui/menu']"
    ).click()
    navigate_to_website.find_element(By.XPATH, "//a[text()='JQuery UI Menus']").click()
    navigate_to_website.find_element(By.XPATH, "//a[text()='Demos']").click()
    navigate_to_website.find_element(
        By.XPATH, "//div[@id='sidebar']//a[text()='Resizable']"
    ).click()
    action = ActionChains(navigate_to_website)
    iframe = navigate_to_website.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
    navigate_to_website.switch_to.frame(iframe)
    initial_size = navigate_to_website.find_element(
        By.CSS_SELECTOR, "div#resizable"
    ).size
    right_side_of_element = navigate_to_website.find_element(
        By.CSS_SELECTOR, "div.ui-resizable-handle.ui-resizable-e"
    )
    lower_side_of_element = navigate_to_website.find_element(
        By.CSS_SELECTOR, "div.ui-resizable-handle.ui-resizable-s"
    )
    corner_side_of_element = navigate_to_website.find_element(
        By.CSS_SELECTOR, "div.ui-resizable-handle.ui-resizable-se"
    )
    action.drag_and_drop_by_offset(right_side_of_element, 50, 0).perform()
    action.drag_and_drop_by_offset(lower_side_of_element, 0, 50).perform()
    action.move_to_element(corner_side_of_element).click_and_hold().move_by_offset(
        100, 100
    ).release().perform()
    expected_size = {
        "width": initial_size["width"] + 150,
        "height": initial_size["height"] + 150,
    }
    actual_size = navigate_to_website.find_element(
        By.CSS_SELECTOR, "div#resizable"
    ).size
    assert actual_size == expected_size


def test_javascript_alerts(navigate_to_website):
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "a[href='/javascript_alerts']"
    ).click()
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "button[onclick='jsAlert()']"
    ).click()
    navigate_to_website.switch_to.alert.accept()
    result = navigate_to_website.find_element(By.CSS_SELECTOR, "p#result")
    assert "You successfully clicked an alert" == result.text
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "button[onclick='jsConfirm()']"
    ).click()
    navigate_to_website.switch_to.alert.accept()
    assert "You clicked: Ok" == result.text
    navigate_to_website.find_element(
        By.CSS_SELECTOR, "button[onclick='jsPrompt()']"
    ).click()
    navigate_to_website.switch_to.alert.send_keys("Hello world!")
    navigate_to_website.switch_to.alert.accept()
    assert "You entered: Hello world!" == result.text


def test_multiple_windows(navigate_to_website):
    wait = WebDriverWait(navigate_to_website, 10)
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/windows']").click()
    navigate_to_website.find_element(By.CSS_SELECTOR, "a[href='/windows/new']").click()
    navigate_to_website.switch_to.window(navigate_to_website.window_handles[1])
    result = navigate_to_website.find_element(By.CSS_SELECTOR, "h3")
    assert "New Window" == result.text
    navigate_to_website.close()
    navigate_to_website.switch_to.window(navigate_to_website.window_handles[0])
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")))
    result_2 = navigate_to_website.find_element(By.CSS_SELECTOR, "h3")
    assert "Opening a new window" == result_2.text
