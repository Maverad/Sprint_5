from locators.locators_authorization import AuthLocators
from locators.locators_success_login import SuccessLoginLocators
import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration(driver, generate):
    driver.find_element(*AuthLocators.log_in_and_registration_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.no_account_button))).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.element_to_be_clickable(AuthLocators.create_account_button))
    driver.find_element(*AuthLocators.email_input).send_keys(generate['email'])
    password = generate['password']
    driver.find_element(*AuthLocators.password_input).send_keys(password)
    driver.find_element(*AuthLocators.submit_password).send_keys(password)
    driver.find_element(*AuthLocators.create_account_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located(SuccessLoginLocators.account_name_after_authorization))
    
    assert driver.find_element(*SuccessLoginLocators.account_name_after_authorization).text == 'User.'
    assert driver.find_element(*SuccessLoginLocators.profile_image_button).is_displayed()