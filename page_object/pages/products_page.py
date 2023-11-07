from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.Locators import LocatorsProducts


class Products(BasePage, LocatorsProducts):


    def verify_dropdown_sorting_a_z(self):
        dropdown = self.find(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text("Name (A to Z)")
        product_name = []
        products_locator = (
            By.XPATH,
            self.PRODUCTS_TEMPLATE.replace("name_of_goods", "*"),
        )
        products = self.find_all(products_locator)
        for product in products:
            product_name.append(product.text)
        sorted_name = sorted(product_name)
        assert sorted_name == product_name, "A-Z sorting is incorrect"

    def verify_dropdown_sorting_z_a(self):
        dropdown = self.find(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text("Name (Z to A)")
        product_name = []
        products_locator = (
            By.XPATH,
            self.PRODUCTS_TEMPLATE.replace("name_of_goods", "*"),
        )
        products = self.find_all(products_locator)
        for product in products:
            product_name.append(product.text)
        sorted_name = sorted(product_name, reverse=True)
        assert sorted_name == product_name, "Z-A sorting is incorrect"

    def verify_dropdown_sorting_low_to_high(self):
        dropdown = self.find(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("lohi")
        prices_list = []
        prices = self.find_all(self.DIV_PRICE)
        for price in prices:
            prices_list.append(float(price.text.replace("$", "")))
        sorted_list = sorted(prices_list)
        assert sorted_list == prices_list, "Price (low to high) sorting is incorrect"

    def verify_dropdown_sorting_high_to_low(self):
        dropdown = self.find(self.DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("hilo")
        prices_list = []
        prices = self.find_all(self.DIV_PRICE)
        for price in prices:
            prices_list.append(float(price.text.replace("$", "")))
        sorted_list = sorted(prices_list, reverse=True)
        assert sorted_list == prices_list, "Price (high to low) sorting is incorrect"

    def click_product(self, name):
        product_locator = (By.XPATH, self.PRODUCTS_TEMPLATE.format(name))
        self.find(product_locator).click()
        self.wait_for_visibility(product_locator)
        div_info = self.find(product_locator)
        assert name in div_info.text, f"Expected text '{name}' not found in element"

    def add_product_to_card(self, name):
        add_locator = (By.CSS_SELECTOR, self.ADD_TO_CART_TEMPLATE.format(name))
        self.find(add_locator).click()
        remove_locator = (By.CSS_SELECTOR, self.REMOVE_TEMPLATE.format(name))
        assert self.is_visible(remove_locator)

    def remove_product(self, name):
        remove_locator = (By.CSS_SELECTOR, self.REMOVE_TEMPLATE.format(name))
        self.find(remove_locator).click()
        add_locator = (By.CSS_SELECTOR, self.ADD_TO_CART_TEMPLATE.format(name))
        assert self.is_visible(add_locator)

    def is_url_matches(self):
        return self.driver.current_url == self.URL
