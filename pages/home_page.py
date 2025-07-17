# pages/home_page.py
# Handles interactions on the homepage like verifying navigation and clicking menu items or brand filters.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    HomePage class represents the main landing page.
    It contains locators and methods for interacting with elements on this page,
    such as navigation links and login status indicators.
    """

    # Locators for elements on the Home Page
    SIGNUP_LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    LOGGED_IN_USERNAME_TEXT = (By.CSS_SELECTOR, "li:nth-child(10) > a")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a[href='/products']")

    def __init__(self, driver):
        """
        Initializes the HomePage by calling the constructor of the BasePage.
        :param driver: The Selenium WebDriver instance.
        """
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_signup_login_button(self):
        """
        Clicks the 'Signup / Login' button in the header, navigating to the login/signup page.
        """
        self.click_element(self.SIGNUP_LOGIN_BUTTON)

    def click_products_button(self):
        """
        Clicks the 'Products' button in the header navigation bar.
        This navigates the user to the products listing page.
        """
        self.click_element(self.PRODUCTS_BUTTON)

    def click_brand(self, brand_name):
        """
        Scrolls to the Brands section and clicks on the specified brand.
        """
        self.driver.execute_script("window.scrollBy(0, 1000);")
        brand_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, brand_name)))
        brand_link.click()

    def get_logged_in_username_text(self):
        """
        Returns the visible text of the 'Logged in as username' element.
        :return: The text string of the logged-in user's name.
        """
        return self.get_element_text(self.LOGGED_IN_USERNAME_TEXT)

    def is_user_logged_in(self, username):
        """
        Checks if the 'Logged in as username' element is displayed and contains the expected username.
        :param username: The expected username string to verify.
        :return: True if the user is logged in with the given username, False otherwise.
        """
        if self.is_element_displayed(self.LOGGED_IN_USERNAME_TEXT):
            displayed_text = self.get_logged_in_username_text()
            return username in displayed_text
        return False

    def click_logout_button(self):
        """
        Clicks the 'Logout' button in the header.
        """
        self.click_element(self.LOGOUT_BUTTON)
