# tests/test_registration.py
# Tests the new user registration process and subsequent login functionality.

import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.config import BASE_URL
import random
import string # Keep this for generate_random_string/email in test if RegisterPage doesn't have it.

class TestUserRegistration:
    # The 'driver' argument here will automatically receive the yielded value
    # from your 'setup_teardown' fixture defined in conftest.py
    def test_new_user_registration_and_login_verification(self, setup_teardown): # Renamed to setup_teardown here to match fixture
        # Now, setup_teardown is the actual driver object
        driver = setup_teardown

        # Initialize page objects within the test method or a custom setup
        home_page = HomePage(driver)
        register_page = RegisterPage(driver)
        home_page.go_to_url(BASE_URL)

        # Generate unique user data for each test run to avoid conflicts
        user_name = register_page.generate_random_string(10)
        user_email = register_page.generate_random_email()
        user_password = "SecurePassword123!" # A strong, consistent password for testing

        # Test Scenario: New User Registration and Login Verification
        # Steps:
        # 1. Register a new user with valid credentials.
        home_page.click_signup_login_button()
        register_page.enter_signup_details(user_name, user_email)

        register_page.fill_account_details(user_password, "15", "7", "1990")
        register_page.fill_address_details(
            "TestFN", "TestLN", "TestCompany", "123 Main St", "Apt 101",
            "United States", "California", "Los Angeles", "90210", "1234567890"
        )

        # 2. Verify successful registration and automatic login.
        assert register_page.is_account_created_message_displayed(), \
            "Account Created message was not displayed after registration."

        register_page.click_continue_button()

        assert home_page.is_user_logged_in(user_name), \
            f"User '{user_name}' is not automatically logged in after registration."

        # 3. Verify the user can log out and then log in successfully with the newly created credentials.
        home_page.click_logout_button()

        assert home_page.is_element_displayed(home_page.SIGNUP_LOGIN_BUTTON), \
            "Signup/Login button not visible after logout, implying logout failed."

        home_page.click_signup_login_button()
        register_page.login_user(user_email, user_password)

        assert home_page.is_user_logged_in(user_name), \
            f"User '{user_name}' failed to log in with newly created credentials."