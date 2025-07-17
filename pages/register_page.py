# pages/register_page.py
# Manages the user registration process including filling forms and submitting them.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage # <-- Original absolute import
import random
import string

class RegisterPage(BasePage):
    NEW_USER_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    NEW_USER_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    MR_RADIO_BUTTON = (By.ID, "id_gender1")
    MRS_RADIO_BUTTON = (By.ID, "id_gender2")
    PASSWORD_INPUT = (By.ID, "password")
    DAYS_DROPDOWN = (By.ID, "days")
    MONTHS_DROPDOWN = (By.ID, "months")
    YEARS_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")

    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS1_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    ACCOUNT_CREATED_MESSAGE = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def generate_random_string(self, length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def generate_random_email(self):
        return f"testuser_{self.generate_random_string(10)}@example.com"

    def enter_signup_details(self, name, email):
        self.enter_text(self.NEW_USER_NAME_INPUT, name)
        self.enter_text(self.NEW_USER_EMAIL_INPUT, email)
        self.click_element(self.SIGNUP_BUTTON)

    def fill_account_details(self, password, day, month, year):
        self.click_element(self.MR_RADIO_BUTTON)
        self.enter_text(self.PASSWORD_INPUT, password)
        Select(self.find_element(self.DAYS_DROPDOWN)).select_by_value(day)
        Select(self.find_element(self.MONTHS_DROPDOWN)).select_by_value(month)
        Select(self.find_element(self.YEARS_DROPDOWN)).select_by_value(year)

    def fill_address_details(self, first_name, last_name, company, address1, address2,
                             country, state, city, zipcode, mobile_number):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.COMPANY_INPUT, company)
        self.enter_text(self.ADDRESS1_INPUT, address1)
        self.enter_text(self.ADDRESS2_INPUT, address2)
        Select(self.find_element(self.COUNTRY_DROPDOWN)).select_by_visible_text(country)
        self.enter_text(self.STATE_INPUT, state)
        self.enter_text(self.CITY_INPUT, city)
        self.enter_text(self.ZIPCODE_INPUT, zipcode)
        self.enter_text(self.MOBILE_NUMBER_INPUT, mobile_number)
        self.click_element(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created_message_displayed(self):
        return self.is_element_displayed(self.ACCOUNT_CREATED_MESSAGE)

    def click_continue_button(self):
        self.click_element(self.CONTINUE_BUTTON)

    def login_user(self, email, password):
        self.enter_text(self.LOGIN_EMAIL_INPUT, email)
        self.enter_text(self.LOGIN_PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)