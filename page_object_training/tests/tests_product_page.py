from page_object_training.pages.product_page import ProductsPage


def test_click_add_product_to_cart(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-backpack")


def test_click_remove_button(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.add_product_to_cart("sauce-labs-onesie")
    product_page.click_remove_product("sauce-labs-onesie")


def test_click_product(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.click_product("Sauce Labs Bike Light")


def test_sorting_a_z(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.verify_dropdown_sorting_a_z()


def test_sorting_z_a(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.verify_dropdown_sorting_z_a()


def test_sorting_low_to_high(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.verify_sorting_low_to_high()


def test_sorting_high_to_low(logged_in_user):
    product_page = ProductsPage(logged_in_user.driver)
    product_page.verify_sorting_high_to_low()






