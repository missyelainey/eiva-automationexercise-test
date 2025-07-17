# pages/base_page.py
# Provides foundational methods used by all other page objects.
# It encapsulates common Selenium operations such as clicking elements, sending keys, scrolling, and waiting.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def click_element(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        return self.find_element(by_locator).text

    def is_element_displayed(self, by_locator):
        try:
            return self.find_element(by_locator).is_displayed()
        except:
            return False

    def scroll_to_element(self, by, value):
        """
        Scroll smoothly to an element by locator.
        Example: scroll_to_element(By.CSS_SELECTOR, ".brands_products")
        """
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
