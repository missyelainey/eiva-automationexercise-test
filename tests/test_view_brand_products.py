# tests/test_view_brand_products.py
# Tests filtering products by brand and verifying if products displayed match the selected brand.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import BASE_URL

class TestViewBrandProducts:
    """
    Test Scenario #3: View and Cart Brand Products
    """

    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.go_to_url(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def test_view_and_cart_brand_products(self):
        brand_to_test = "Polo"  # Can change to "Madame", "H&M", etc.
        expected_product_name = "Polo T-Shirt"  # Update based on actual brand product on site

        # Step 1: Click "Products"
        self.home_page.click_products_button()

        # Step 2: Verify brand sidebar is visible
        assert self.product_page.is_brand_sidebar_present(), "Brand sidebar is not visible"

        # Step 3: Click the specific brand link
        assert self.product_page.click_brand_by_name(brand_to_test), f"Failed to click on brand: {brand_to_test}"

        # Step 4: Verify the brand's product page is displayed
        assert self.product_page.is_brand_page_displayed(brand_to_test), f"Brand page for {brand_to_test} not displayed"

        # Step 5: Add a product of that brand to the cart
        assert self.product_page.add_product_to_cart_by_name(expected_product_name), \
            f"Failed to add brand product '{expected_product_name}' to cart"

        # Step 6: View cart and confirm the product is there
        self.product_page.click_view_cart_in_modal()
        assert self.cart_page.is_product_in_cart(expected_product_name), \
            f"Product '{expected_product_name}' was not found in the cart"
