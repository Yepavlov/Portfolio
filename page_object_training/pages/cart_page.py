from selenium.webdriver.common.by import By

from page_object_training.pages.base_page import BasePage
from page_object_training.pages.locators import CommonLocators, LocatorsCartPage


class CartPage(BasePage, CommonLocators, LocatorsCartPage):

    def check_added_products(self, product_names):
        self.wait_for_visibility(self.ALL_PRODUCTS_IN_CART_CSS_SELECTOR)
        product_names_list = self.find_all_els(self.ALL_PRODUCTS_IN_CART_CSS_SELECTOR)
        actual_product_names = [name.text for name in product_names_list]
        print("Actual product names: ", actual_product_names)
        print("Expected product names: ", product_names)
        assert actual_product_names == product_names

    def verify_number_of_added_products_on_the_cart_icon(self, product_names):
        cart = self.find_el(self.CART)
        expected_number_of_products = len(product_names)
        actual_number_of_products = int(cart.text)
        print(f"Expected number is: {expected_number_of_products}, actual number is: {actual_number_of_products}")
        assert expected_number_of_products == actual_number_of_products

    def click_remove_product_from_the_cart(self, product_names):
        for name in product_names:
            remove_locator = (By.CSS_SELECTOR, self.BUTTON_REMOVE_CSS_SELECTOR.format(name=name))
            self.find_el(remove_locator).click()
            self.wait_for_element_to_disappear(remove_locator)
            print(f"Product: {name} successfully removed from the cart")

    def click_checkout_button(self):
        self.find_el(self.BUTTON_CHECKOUT).click()

    def fill_in_your_information(self, first_name=None, last_name=None, postal_code=None):
        if first_name is not None:
            self.find_el(self.FIELD_FIRST_NAME).send_keys(first_name)
        if last_name is not None:
            self.find_el(self.FIELD_LAST_NAME).send_keys(last_name)
        if postal_code is not None:
            self.find_el(self.FIELD_POSTAL_CODE).send_keys(postal_code)

        self.find_el(self.BUTTON_CONTINUE).click()

        if first_name is not None and last_name is not None and postal_code is not None:
            assert "Checkout: Overview" == self.find_el(self.DIV_CHECKOUT_OVERVIEW).text
        elif first_name is None and last_name is None and postal_code is None:
            assert "Error: First Name is required" == self.find_el(self.ERROR_MESSAGE_CONTAINER).text
        elif first_name is None:
            assert "Error: First Name is required" == self.find_el(self.ERROR_MESSAGE_CONTAINER).text
        elif last_name is None:
            assert "Error: Last Name is required" == self.find_el(self.ERROR_MESSAGE_CONTAINER).text
        elif postal_code is None:
            assert "Error: Postal Code is required" == self.find_el(self.ERROR_MESSAGE_CONTAINER).text

    def check_price_total(self):
        """
        Tax = 8%
        """
        price_list_float = []
        price_list = self.find_all_els(self.DIV_ITEM_PRICE)
        for price in price_list:
            price_list_float.append(float(price.text.replace("$", "")))
        expected_total_price_without_tax = sum(price_list_float)
        expected_tax = expected_total_price_without_tax * 0.08
        expected_total_price = expected_total_price_without_tax + expected_tax
        actual_total_price_without_tax = float(self.find_el(self.DIV_ITEM_TOTAL).
                                               text.replace("Item total: $", "").strip())
        actual_tax = float(self.find_el(self.DIV_TAX_TOTAL).text.replace("Tax: $", "").strip())
        actual_total_price = float(self.find_el(self.DIV_TOTAL).text.replace("Total: $", "").strip())
        print(f"Expected total price without tax: {expected_total_price_without_tax} and"
              f"actual total price without tax: {actual_total_price_without_tax}")
        assert expected_total_price_without_tax == actual_total_price_without_tax, \
            f"Expected total price without tax: {expected_total_price_without_tax} isn't equal to" \
            f"actual total price without tax: {actual_total_price_without_tax}"
        print(f"Expected tax: {round(expected_tax, 2)} and actual tax: {actual_tax}")
        assert round(expected_tax, 2) == actual_tax, f"Expected tax: {expected_tax} " \
                                                     f"isn't equal to actual tax: {actual_tax}"
        print(f"Expected total price: {round(expected_total_price, 2)} and actual total price: {actual_total_price}")
        assert round(expected_total_price, 2) == actual_total_price, f"Expected total price: {expected_total_price} " \
                                                                     f"isn't equal to " \
                                                                     f"actual total price: {actual_total_price}"

    def click_button_finish(self):
        self.find_el(self.BUTTON_FINISH).click()
        self.wait_for_visibility(self.BUTTON_BACK_HOME)
        assert self.is_visible(self.BUTTON_BACK_HOME)


