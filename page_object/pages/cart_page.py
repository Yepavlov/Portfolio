from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage


class CartPage(BasePage):
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
