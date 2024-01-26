from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object_training.pages.base_page import BasePage
from page_object_training.pages.locators import CommonLocators, LocatorsProducts


class ProductsPage(BasePage, CommonLocators, LocatorsProducts):
    """
    name of product xpath = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                            "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    name of product css_selector = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt",
                            "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test\.allthethings\(\)-t-shirt-\(red\)"]
    """

    def add_product_to_cart(self, name_of_product):
        add_product_locator = (By.CSS_SELECTOR, self.ADD_TO_CART_TEMPLATE_CSS_SELECTOR.format(name_of_product))
        self.find_el(add_product_locator).click()
        remove_product_locator = (By.CSS_SELECTOR, self.REMOVE_TEMPLATE_CSS_SELECTOR.format(name_of_product))
        assert self.is_visible(remove_product_locator)

    def click_product(self, name_of_product):
        product_locator = (By.XPATH, self.PRODUCTS_TEMPLATE_XPATH.format(name_of_product))
        product = self.find_el(product_locator)
        product.click()
        product_details_locator = (By.XPATH, self.PRODUCTS_DETAILS_TEMPLATE_XPATH.format(name_of_product))
        product_details = self.find_el(product_details_locator)
        self.wait_for_visibility(self.BUTTON_BACK_TO_PRODUCTS)
        assert self.is_visible(self.BUTTON_BACK_TO_PRODUCTS) and name_of_product in product_details.text

    def click_remove_product(self, name_of_product):
        remove_product_locator = (By.CSS_SELECTOR, self.REMOVE_TEMPLATE_CSS_SELECTOR.format(name_of_product))
        self.find_el(remove_product_locator).click()
        add_product_locator = (By.CSS_SELECTOR, self.ADD_TO_CART_TEMPLATE_CSS_SELECTOR.format(name_of_product))
        assert self.is_visible(add_product_locator)

    def verify_dropdown_sorting_a_z(self):
        dropdown = self.find_el(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("az")
        product_names = []
        product_locators = (By.XPATH, self.PRODUCTS_TEMPLATE_XPATH.replace("name_of_product", "*"))
        products = self.find_all_els(product_locators)
        for product in products:
            product_names.append(product.text)
        expected_result = sorted(product_names)
        assert expected_result == product_names, "Sorting A-Z is incorrect"

    def verify_dropdown_sorting_z_a(self):
        dropdown = self.find_el(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("za")
        product_names = []
        product_locators = (By.XPATH, self.PRODUCTS_TEMPLATE_XPATH.replace("name_of_product", "*"))
        products = self.find_all_els(product_locators)
        for product in products:
            product_names.append(product.text)
        expected_result = sorted(product_names, reverse=True)
        assert expected_result == product_names, "Sorting Z-A is incorrect"

    def verify_sorting_low_to_high(self):
        dropdown = self.find_el(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("lohi")
        product_prices_list = []
        prices = self.find_all_els(self.DIV_PRICE)
        for price in prices:
            product_prices_list.append(float(price.text.replace("$", "")))
        expected_result = sorted(product_prices_list)
        assert expected_result == product_prices_list, "Sorting Low to High is incorrect"

    def verify_sorting_high_to_low(self):
        dropdown = self.find_el(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("hilo")
        product_prices_list = []
        prices = self.find_all_els(self.DIV_PRICE)
        for price in prices:
            product_prices_list.append(float(price.text.replace("$", "")))
        expected_result = sorted(product_prices_list, reverse=True)
        assert expected_result == product_prices_list, "Sorting High to Low is incorrect"

    def is_url_matches(self) -> bool:
        return self.driver.current_url == self.URL



