from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.Locators import LocatorsCartPage


class CartPage(BasePage, LocatorsCartPage):

    def check_added_goods(self, names_to_check):
        for name in names_to_check:
            locator = (By.XPATH, self.NAME_GOODS_IN_CARD_PATH.format(name=name))
            if not self.is_visible(locator):
                return False
        return True

    def remove_from_the_cart(self, name):
        locator = (By.CSS_SELECTOR, self.BUTTON_REMOVE.format(name=name))
        self.find(locator).click()

    def check_remove_good(self, name):
        locator = (By.XPATH, self.NAME_GOODS_IN_CARD_PATH.format(name=name))
        try:
            self.wait_for_invisibility(locator)
            return True
        except TimeoutException:
            return False

    def click_button_ckeckout(self):
        self.find(self.BUTTON_CHECKOUT).click()

    def fill_in_your_information(self, name, last_name, postal_code):
        self.find(self.FIELD_FIRST_NAME).send_keys(name)
        self.find(self.FIELD_LAST_NAME).send_keys(last_name)
        self.find(self.FIELD_POSTAL_CODE).send_keys(postal_code)
        self.find(self.BUTTON_CONTINUE).click()
        assert "Checkout: Overview" in self.find(self.DIV_CHECKOUT_OVERVIEW).text

    def fill_in_your_information_without_name_field(self, last_name, postal_code):
        self.find(self.FIELD_LAST_NAME).send_keys(last_name)
        self.find(self.FIELD_POSTAL_CODE).send_keys(postal_code)
        self.find(self.BUTTON_CONTINUE).click()
        assert "Error: First Name is required" in self.find(self.VALIDATION_ERROR_MESSAGE).text

    def fill_in_your_information_without_last_name_field(self, name, postal_code):
        self.find(self.FIELD_FIRST_NAME).send_keys(name)
        self.find(self.FIELD_POSTAL_CODE).send_keys(postal_code)
        self.find(self.BUTTON_CONTINUE).click()
        assert "Error: Last Name is required" in self.find(self.VALIDATION_ERROR_MESSAGE).text

    def fill_in_your_information_without_postal_code_field(self, name, last_name):
        self.find(self.FIELD_FIRST_NAME).send_keys(name)
        self.find(self.FIELD_LAST_NAME).send_keys(last_name)
        self.find(self.BUTTON_CONTINUE).click()
        assert "Error: Postal Code is required" in self.find(self.VALIDATION_ERROR_MESSAGE).text

    def check_the_correct_total(self):
        prices_list = []
        prices = self.find_all(self.DIV_ITEM_PRICE)
        for price in prices:
            prices_list.append(float(price.text.replace("$", "")))
        total_text = self.find(self.DIV_TOTAL_COST).text
        actual_total_price = float(
            total_text.replace("Total:", "").replace("$", "").strip()
        )
        tax_percentage = 0.08
        tax_amount = sum(prices_list) * tax_percentage
        expected_total = sum(prices_list) + tax_amount
        assert actual_total_price == round(expected_total, 2), "Incorrect total price"

    def check_click_button_finish(self):
        self.find(self.BUTTON_FINISH).click()
        assert "Your order has been dispatched, " \
               "and will arrive just as fast " \
               "as the pony can get there!" in self.find(self.INFORMATION_ORDER_IS_DISPATCHED).text


    def check_click_button_back_home(self, expected_url):
        self.find(self.BUTTON_BACK_HOME).click()
        self.check_current_url(expected_url)
