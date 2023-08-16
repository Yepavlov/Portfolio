from page_object.pages.products_page import Products


def test_check_sorting_a_z(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.click_dropdown_sorting_a_z()


def test_check_sorting_z_a(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.click_dropdown_sorting_z_a()


def test_check_sorting_low_to_high(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.click_dropdown_sorting_low_to_high()


def test_check_sorting_high_to_low(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.click_dropdown_sorting_high_to_low()


def test_click_product(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.click_product("Sauce Labs Onesie")


def test_add_and_remove_product_from_products_page(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.add_product_to_card("sauce-labs-bike-light")
    products_page.remove_product("sauce-labs-bike-light")
