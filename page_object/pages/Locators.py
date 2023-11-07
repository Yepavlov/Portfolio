from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    USER_NAME = (By.CSS_SELECTOR, "input#user-name")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    LOGIN = (By.CSS_SELECTOR, "input#login-button")
    CART = (By.CSS_SELECTOR, "a.shopping_cart_link")
    DIV_USER_AND_PASSWORD_DNT_MATCH = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: "
        "Username and password do not match any user in this service')]",
    )
    DIV_LOCKED_USER = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: Sorry, this user has been locked out.')]",
    )
    DIV_USERNAME_IS_REQUIRED = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: Username is required')]",
    )
    DIV_PASSWORD_IS_REQUIRED = (
        By.XPATH,
        "//*[contains(text(), 'Epic sadface: Password is required')]",
    )

class LocatorsCartPage:
    NAME_GOODS_IN_CARD_PATH = "//div[text()='{name}']"

    BUTTON_REMOVE = "button#remove-{name}"

    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "button#checkout")
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "input#first-name")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "input#last-name")
    FIELD_POSTAL_CODE = (By.CSS_SELECTOR, "input#postal-code")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "input#continue")
    DIV_CHECKOUT_OVERVIEW = (By.CSS_SELECTOR, "span.title")
    DIV_TOTAL_COST = (By.CSS_SELECTOR, "div.summary_info_label.summary_total_label")
    DIV_ITEM_PRICE = (By.CSS_SELECTOR, "div.inventory_item_price")


class LocatorsProducts:
    """
    name of product xpath = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                            "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    name of product css = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt",
                            "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test\.allthethings\(\)-t-shirt-\(red\)"]
    """

    PRODUCTS_TEMPLATE = "//*[contains(text(), '{}')]"
    ADD_TO_CART_TEMPLATE = "button#add-to-cart-{}"
    REMOVE_TEMPLATE = "button#remove-{}"

    DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")

    DIV_PRICE = (By.CSS_SELECTOR, "div.inventory_item_price")

    URL = "https://www.saucedemo.com/inventory.html"