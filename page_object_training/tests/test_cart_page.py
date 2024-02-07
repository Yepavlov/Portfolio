from page_object_training.pages.cart_page import CartPage
from page_object_training.pages.product_page import ProductsPage


def test_check_added_products_in_the_cart(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])


def test_number_of_products_on_the_icon_cart(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.verify_number_of_added_products_on_the_cart_icon(["sauce-labs-backpack", "sauce-labs-bike-light"])


def test_click_remove_from_the_cart(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    cart_page.click_remove_product_from_the_cart(["sauce-labs-backpack", "sauce-labs-bike-light"])


def test_fill_in_your_information(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    cart_page.click_checkout_button()
    cart_page.fill_in_your_information("Jordan", "Tramp", "96130")


def test_fill_in_your_information_without_first_name(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    cart_page.click_checkout_button()
    cart_page.fill_in_your_information(first_name=None, last_name="Tramp", postal_code="96130")


def test_fill_in_your_information_without_last_name(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    cart_page.click_checkout_button()
    cart_page.fill_in_your_information(first_name="Jordan", last_name=None, postal_code="96130")


def test_fill_in_your_information_without_postal_code(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    cart_page.click_checkout_button()
    cart_page.fill_in_your_information(first_name="Jordan", last_name="Tramp", postal_code=None)


def test_fill_in_your_information_without_required_fields(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    cart_page.click_checkout_button()
    cart_page.fill_in_your_information(first_name=None, last_name=None, postal_code=None)


def test_check_price_total(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.check_added_products(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    cart_page.click_checkout_button()
    cart_page.fill_in_your_information("Jordan", "Tramp", "96130")
    cart_page.check_price_total()


def test_click_button_finish(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")
    product_page.add_product_to_cart("sauce-labs-bike-light")
    product_page.click_go_to_cart()
    cart_page = CartPage(logged_in_user.driver)
    cart_page.click_checkout_button()
    cart_page.fill_in_your_information("Jordan", "Tramp", "96130")
    cart_page.click_button_finish()
