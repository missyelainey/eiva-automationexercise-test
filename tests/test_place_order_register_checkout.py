# tests/test_place_order_register_checkout.py
# Automates the end-to-end flow where a new user registers
# during checkout, places an order, and verifies order completion.

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class TestPlaceOrderRegisterWhileCheckout:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com/")
        self.wait = WebDriverWait(self.driver, 15)

        # Page object placeholders — replace with actual page class usage if applicable
        from pages.home_page import HomePage
        from pages.product_page import ProductPage
        from pages.cart_page import CartPage

        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def generate_random_email(self):
        import random, string
        return f"testuser_{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}@mail.com"

    def test_place_order_register_during_checkout(self):
        product_name = "Pure Cotton V-Neck T-Shirt"

        # Step 1: Add product to cart
        self.home_page.click_products_button()
        assert self.product_page.add_product_to_cart_by_name(product_name)
        self.product_page.click_view_cart_in_modal()

        # Step 2: Click Proceed to Checkout
        self.cart_page.click_proceed_to_checkout()

        # Step 3: Click Register / Login
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//u[normalize-space()='Register / Login']"))).click()

        # Step 4: Register a new user
        name = "Eiva Tester"
        email = self.generate_random_email()
        self.wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//button[text()='Signup']").click()

        # Fill minimal signup form
        self.wait.until(EC.presence_of_element_located((By.ID, "id_gender2"))).click()
        self.driver.find_element(By.ID, "password").send_keys("testpass123")
        self.driver.find_element(By.ID, "days").send_keys("1")
        self.driver.find_element(By.ID, "months").send_keys("January")
        self.driver.find_element(By.ID, "years").send_keys("2000")
        self.driver.find_element(By.ID, "first_name").send_keys("Eiva")
        self.driver.find_element(By.ID, "last_name").send_keys("Tester")
        self.driver.find_element(By.ID, "address1").send_keys("123 Test Street")
        self.driver.find_element(By.ID, "state").send_keys("Metro")
        self.driver.find_element(By.ID, "city").send_keys("Manila")
        self.driver.find_element(By.ID, "zipcode").send_keys("1234")
        self.driver.find_element(By.ID, "mobile_number").send_keys("09999999999")
        self.driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

        # Step 5: Verify account created
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//b[normalize-space()='Account Created!']")))
        self.driver.find_element(By.XPATH, "//a[text()='Continue']").click()

        # Optional: Handle modal/ads that might block the UI
        try:
            self.wait.until(EC.invisibility_of_element_located((By.ID, "ad")) or EC.alert_is_present())
        except:
            pass

        # Step 6: Return to cart manually, then proceed again
        self.driver.get("https://automationexercise.com/view_cart")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Proceed To Checkout']"))).click()

        # Step 7: Add comment and click Place Order
        message_box = self.wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']")))
        message_box.clear()
        message_box.send_keys("Test order during checkout.")

        # Fix: Scroll to Place Order and click using JavaScript
        place_order_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Place Order']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", place_order_btn)
        self.driver.execute_script("arguments[0].click();", place_order_btn)

        # Step 8: Verify that the payment page is displayed
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Payment']")))
        print("Successfully navigated to payment page.")

