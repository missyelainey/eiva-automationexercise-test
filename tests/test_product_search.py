# tests/test_product_search.py
# Validates that a user can search for a product by keyword and add it to the cart.

import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import BASE_URL

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


class TestProductSearchAndAddToCart:
    """
    Test suite for product search and adding items to the shopping cart.
    """

    def setup_method(self, method):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # To use Firefox, uncomment the line below and comment out the Chrome line above.
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.go_to_url(BASE_URL)

    def teardown_method(self, method):
        if self.driver:
            self.driver.quit()

    def test_product_search_and_add_to_cart(self):
        """
        Tests the process of searching for a product, verifying its display in results,
        and successfully adding it to the shopping cart.
        """
        # --- Test Data ---
        search_term = "T-shirt" # Search term as per requirement
        product_name_to_verify = "Pure Cotton V-Neck T-Shirt"


        # IMPORTANT: Updated product_id_to_add and product_name_to_verify based on your last screenshot.
        # This corresponds to "Pure Cotton V-Neck T-Shirt" with data-product-id="1".
        product_id_to_add = "1"
        product_name_to_verify = "Pure Cotton V-Neck T-Shirt"

        # --- Test Scenario Steps and Assertions ---

        # Step 0: Navigate to the Products page first.
        self.home_page.click_products_button()

        # Step 1: Search for a specific product (e.g., "T-shirt").
        self.product_page.search_product(search_term)

        # Step 2: Verify that relevant products are displayed.
        assert self.product_page.is_product_displayed_in_results(product_name_to_verify), \
            f"Product '{product_name_to_verify}' was not displayed in search results after performing search."

        # Step 3: Add the specific product (Pure Cotton V-Neck T-Shirt) to the shopping cart.
        assert self.product_page.add_product_to_cart_by_name(product_name_to_verify), \
            f"Failed to add '{product_name_to_verify}' to cart."

        # Handle the "Added!" confirmation modal and click 'View Cart'.
        self.product_page.click_view_cart_in_modal()

        # Step 4: Verify the product is successfully added to the cart and the cart total is updated.
        assert self.cart_page.is_product_in_cart(product_name_to_verify), \
            f"Product '{product_name_to_verify}' was not found in the shopping cart after adding it."

        # Optional: Add more assertions here, such as verifying the quantity or the cart's total price.
        # Example: assert "Rs." in self.cart_page.get_cart_total(), "Cart total currency not displayed correctly."
