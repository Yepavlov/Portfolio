

from selenium.webdriver.common.by import By


class CommonLocators:
    BURGER_MENU_BTN = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a#logout_sidebar_link")
    CART = (By.CSS_SELECTOR, "a.shopping_cart_link")


class LocatorsLoginPage:
    USER_NAME = (By.CSS_SELECTOR, "input#user-name")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input#login-button")
    DIV_ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-message-container.error")


class LocatorsCartPage:
    PRODUCT_NAME_IN_CART_PATH_XPATH = "//div[text()='{name}']"
    ALL_PRODUCTS_IN_CART_CSS_SELECTOR = (By.CSS_SELECTOR, "div.inventory_item_name")

    BUTTON_REMOVE_CSS_SELECTOR = "button#remove-{name}"

    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "button#checkout")
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "input#first-name")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "input#last-name")
    FIELD_POSTAL_CODE = (By.CSS_SELECTOR, "input#postal-code")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "input#continue")
    DIV_CHECKOUT_OVERVIEW = (By.CSS_SELECTOR, "span.title")
    DIV_ITEM_PRICE = (By.CSS_SELECTOR, "div.inventory_item_price")
    DIV_ITEM_TOTAL = (By.CSS_SELECTOR, "div.summary_subtotal_label")
    DIV_TAX_TOTAL = (By.CSS_SELECTOR, "div.summary_tax_label")
    DIV_TOTAL = (By.CSS_SELECTOR, "div.summary_info_label.summary_total_label")
    ERROR_MESSAGE_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")
    BUTTON_FINISH = (By.CSS_SELECTOR, "button#finish")
    INFORMATION_ORDER_IS_DISPATCHED = (By.CSS_SELECTOR, "div.complete-text")
    BUTTON_BACK_HOME = (By.CSS_SELECTOR, "button#back-to-products")


class LocatorsProducts:
    """
    name of product xpath = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                            "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    name of product css_selector = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt",
                            "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test\.allthethings\(\)-t-shirt-\(red\)"]
    """

    PRODUCTS_TEMPLATE_XPATH = "//div[@class='inventory_item_name ' and contains(text(), '{}')]"
    PRODUCTS_DETAILS_TEMPLATE_XPATH = "//div[@class='inventory_details_name large_size' and contains(text(), '{}')]"
    ADD_TO_CART_TEMPLATE_CSS_SELECTOR = "button#add-to-cart-{}"
    REMOVE_TEMPLATE_CSS_SELECTOR = "button#remove-{}"

    DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")

    DIV_PRICE = (By.CSS_SELECTOR, "div.inventory_item_price")

    URL = "https://www.saucedemo.com/inventory.html"
    BUTTON_BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "button#back-to-products")
