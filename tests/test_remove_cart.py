# tests/test_remove_cart.py
# Ensures users can remove an item from the cart and see an empty cart state.

import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import BASE_URL

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRemoveProductFromCart:
    """
    Test for adding a product to the cart and removing it afterward.
    """

    def setup_method(self, method):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.go_to_url(BASE_URL)

    def teardown_method(self, method):
        if self.driver:
            self.driver.quit()

    def test_remove_product_from_cart(self):
        """
        Adds a product to the cart, then removes it and verifies it's gone.
        """
        product_name = "Pure Cotton V-Neck T-Shirt"

        # Step 1: Go to Products page
        self.home_page.click_products_button()

        # Step 2: Add the product to cart
        assert self.product_page.add_product_to_cart_by_name(product_name), \
            f"Failed to add '{product_name}' to cart."

        self.product_page.click_view_cart_in_modal()

        # Step 3: Verify product is in cart
        assert self.cart_page.is_product_in_cart(product_name), \
            f"'{product_name}' not found in cart after adding."

        # Step 4: Remove product from cart
        self.cart_page.remove_product_by_name(product_name)

        # Step 5: Wait a bit to allow cart UI to update before checking again
        WebDriverWait(self.driver, 5).until_not(
            lambda driver: self.cart_page.is_product_in_cart(product_name)
        )

        # Step 6: Verify product is removed
        assert not self.cart_page.is_product_in_cart(product_name), \
            f"'{product_name}' still found in cart after removal."
