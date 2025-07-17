# pages/product_page.py
# Handles product listings including adding products to cart and filtering by brand.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class ProductPage(BasePage):

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULT_PRODUCTS = (By.CSS_SELECTOR, ".features_items .productinfo.text-center p")
    VIEW_CART_BUTTON_MODAL = (By.XPATH, "//u[normalize-space()='View Cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click_element(self.SEARCH_BUTTON)

    def is_product_displayed_in_results(self, product_name):
        results = self.driver.find_elements(*self.SEARCH_RESULT_PRODUCTS)
        return any(product_name.strip().lower() in r.text.strip().lower() for r in results)

    def add_product_to_cart_by_name(self, product_name):
        """
        Locate the specific product card by name, scroll to it, hover to reveal the Add to Cart button,
        and click it using JavaScript to bypass overlay/interception issues.
        """
        product_cards = self.driver.find_elements(By.CSS_SELECTOR, ".features_items .col-sm-4")

        print(f"Found {len(product_cards)} product cards.")
        for idx, card in enumerate(product_cards, start=1):
            try:
                name_elem = card.find_element(By.CSS_SELECTOR, ".productinfo.text-center p")
                name = name_elem.text.strip()
                print(f"Product {idx}: {name}")

                if product_name.lower() in name.lower():
                    print(f"Match found: {name}. Trying to click 'Add to cart'...")

                    # Scroll into view and hover
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
                    self.actions.move_to_element(card).perform()

                    # Wait for the button to be clickable
                    add_button = card.find_element(By.XPATH, ".//a[contains(@class,'add-to-cart')]")
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, ".//a[contains(@class,'add-to-cart')]")))

                    # Use JS click to avoid overlay issues
                    self.driver.execute_script("arguments[0].click();", add_button)
                    return True
            except Exception as e:
                print(f"Error with product {idx}: {e}")
                continue

        print("No matching product found or 'Add to cart' failed.")
        return False

    def click_view_cart_in_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.VIEW_CART_BUTTON_MODAL)).click()

    # Methods for Adding a Product with Brand to Cart and Viewing It
    def is_brand_sidebar_present(self):
        try:
            sidebar = self.driver.find_element(By.CSS_SELECTOR, ".brands_products")
            return sidebar.is_displayed()
        except:
            return False

    def click_brand_by_name(self, brand_name):
        """
        Clicks the brand link in the sidebar that matches the given brand name.
        """
        try:
            brand_links = self.driver.find_elements(By.CSS_SELECTOR, ".brands-name a")
            for link in brand_links:
                if brand_name.strip().lower() in link.text.strip().lower():
                    link.click()
                    return True
        except Exception as e:
            print(f"Error clicking brand: {e}")
        return False

    def is_brand_page_displayed(self, brand_name):
        """
        Checks that the brand-specific page is shown.
        """
        try:
            header = self.driver.find_element(By.CSS_SELECTOR, ".title.text-center")
            return brand_name.lower() in header.text.lower()
        except:
            return False
        
    # Methods for Removing a Product on the Cart
    def remove_product_by_name(self, product_name):
        """
        Clicks the remove (X) button for a product with the given name and waits until it's gone.
        """
        from selenium.common.exceptions import TimeoutException

        product_rows = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        for row in product_rows:
            if product_name in row.text:
                try:
                    remove_button = row.find_element(By.CLASS_NAME, "cart_quantity_delete")
                    self.driver.execute_script("arguments[0].click();", remove_button)

                    # Wait until product no longer appears in cart
                    WebDriverWait(self.driver, 10).until(
                        lambda driver: not self.is_product_in_cart(product_name)
                    )
                    print(f"[Remove] '{product_name}' removed successfully.")
                    return
                except TimeoutException:
                    print(f"[Remove Timeout] '{product_name}' was not removed in time.")
                    return
                except Exception as e:
                    print(f"[Remove Error] Could not remove '{product_name}': {e}")
        print(f"[Remove] '{product_name}' not found in cart.")



