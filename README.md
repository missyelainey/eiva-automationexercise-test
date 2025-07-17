# Automation Exercise - E-commerce Test Suite

This project automates core functionalities of the [AutomationExercise.com](https://automationexercise.com) website using **Python**, **Selenium WebDriver**, and **Pytest**. It covers end-to-end scenarios such as user registration, product search, cart operations, and checkout.

---

## Project Structure
```text
eiva-automationexercise-tests/
│
├── pages/                       # Page Object Models (POM)
│   ├── base_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── register_page.py
│   └── checkout_page.py
│
├── tests/                       # All test cases
│   ├── conftest.py              # Fixtures (e.g., setup/teardown)
│   ├── test_registration.py
│   ├── test_product_search.py
│   ├── test_view_brand_products.py
│   ├── test_remove_cart.py
│   └── test_place_order_register_checkout.py
│
├── utils/                       # Helper functions, config, constants
│   └── config.py
│
├── .gitignore                   # Ignore virtualenvs, pycache, logs, etc.
├── requirements.txt             # All dependencies (selenium, pytest, etc.)
├── README.md                    # Project overview, setup, run instructions
└── pytest.ini (optional)        # Pytest configuration
```

---

## Test Scenarios Covered

| Module                                  | Test Case ID | Test Description                                                              |
|-----------------------------------------|--------------|-------------------------------------------------------------------------------|
| USER REGISTRATION & AUTHENTICATION      | AE-TC01      | Verify if the user can register and login successfully.                       |
| PRODUCT DISCOVERY & CART OPERATIONS     | AE-TC02      | Verify if a user can search for a product and add it to the cart.             |
| BRAND NAVIGATION & FILTERING            | AE-TC03      | Verify if brand-specific products can be viewed and added to cart.            |
| CART ITEM MANAGEMENT                    | AE-TC04      | Verify if a user can remove a product from the shopping cart.                 |
| CHECKOUT PROCESS WITH USER REGISTRATION | AE-TC05      | Verify if a user can register during checkout and place an order.             |

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/eiva_automation_task.git
   cd eiva_automation_task

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run Tests**
   ```bash
   pytest tests/

---

## Tools and Technologies
- Python 3.x
- Selenium WebDriver
- Pytest
- ChromeDriver

---

## Created By
- Elaine Cristel Elleazar
- July 17, 2025
- https://automationexercise.com

---

## Notes
- Ensure ChromeDriver is compatible with your installed Chrome version.
- Adjust timeouts and selectors if the site changes structure.
