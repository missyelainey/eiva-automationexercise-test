# pages/cart_page.py
# Handles interactions and validations on the Cart page
# such as removing products or verifying product presence.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class CartPage(BasePage):
    """
    CartPage class represents the shopping cart page.
    It contains locators and methods for verifying product presence and cart totals.
    """

    # Locators
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "td.cart_description h4 a")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, "#cart_info .total_price")

    def __init__(self, driver):
        super().__init__(driver)

    def is_product_in_cart(self, product_name):
        """
        Checks if the product is listed in the cart.
        """
        try:
            cart_products = self.driver.find_elements(By.CSS_SELECTOR, "td.cart_description h4 a")
            for product in cart_products:
                if product_name.lower() in product.text.strip().lower():
                    print(f"[Cart Check] Found: {product.text.strip()}")
                    return True
            return False
        except:
            return False

    def get_cart_total(self):
        """
        Gets the total price displayed in the cart.
        """
        self.wait.until(EC.visibility_of_element_located(self.CART_TOTAL_PRICE))
        return self.get_element_text(self.CART_TOTAL_PRICE)
    
    def remove_product_by_name(self, product_name):
        """
        Clicks the remove (X) button beside the given product in the cart.
        Waits until the product is no longer visible in the page source.
        """
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tr")

        for row in rows:
            try:
                name_cell = row.find_element(By.CSS_SELECTOR, "td.cart_description h4 a")
                if product_name.lower() in name_cell.text.strip().lower():
                    delete_button = row.find_element(By.CLASS_NAME, "cart_quantity_delete")
                    delete_button.click()

                    # Wait until the product is removed from the cart
                    WebDriverWait(self.driver, 5).until_not(
                        lambda d: product_name.lower() in d.page_source.lower()
                    )
                    break
            except Exception:
                continue

    def click_proceed_to_checkout_button(self):
        checkout_btn = self.driver.find_element(By.CSS_SELECTOR, "a.check_out")
        checkout_btn.click()

    def click_register_login_in_checkout(self):
        link = self.driver.find_element(By.LINK_TEXT, "Register / Login")
        link.click()

    def click_proceed_to_checkout(self):
        button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
        button.click()
