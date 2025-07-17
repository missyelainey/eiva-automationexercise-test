# pages/checkout_page.py
# Manages checkout flow including address confirmation and placing orders.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_logged_in_as(self, name):
        return name.lower() in self.driver.page_source.lower()

    def enter_order_comment(self, comment):
        textarea = self.driver.find_element(By.NAME, "message")
        textarea.send_keys(comment)

    def click_place_order_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "a[href='/payment']")
        button.click()

    def fill_payment_details(self):
        self.driver.find_element(By.NAME, "name_on_card").send_keys("Test User")
        self.driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.find_element(By.NAME, "expiry_month").send_keys("12")
        self.driver.find_element(By.NAME, "expiry_year").send_keys("2028")

    def submit_payment(self):
        self.driver.find_element(By.ID, "submit").click()

    def is_order_success_message_displayed(self):
        return "Your order has been placed successfully!" in self.driver.page_source
