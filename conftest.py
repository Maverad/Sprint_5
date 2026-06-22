import pytest
from selenium import webdriver
import test_data
from locators.locators_authorization import AuthLocators
from locators.locators_success_login import SuccessLoginLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(test_data.Urls.main_url)
    yield driver
    driver.quit()

@pytest.fixture
def generate() -> dict:
    data = {}
    data['email'] = test_data.GenerateData.generate_email()
    data['password']= test_data.GenerateData.generate_password()
    return data

@pytest.fixture
def driver_with_reg():
    driver = webdriver.Chrome()
    driver.get(test_data.Urls.main_url)
    driver.find_element(*AuthLocators.log_in_and_registration_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.log_in_button)))
    driver.find_element(*AuthLocators.email_input).send_keys(test_data.AuthorizationTestData.test_acc_email)
    driver.find_element(*AuthLocators.password_input).send_keys(test_data.AuthorizationTestData.test_acc_password)
    driver.find_element(*AuthLocators.log_in_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((SuccessLoginLocators.account_name_after_authorization)))
    yield driver
    driver.quit()