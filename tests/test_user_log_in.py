from locators.locators_authorization import AuthLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_success_login import SuccessLoginLocators
import test_data

def test_user_log_in(driver):
    driver.find_element(*AuthLocators.log_in_and_registration_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.log_in_button)))
    driver.find_element(*AuthLocators.email_input).send_keys(test_data.AuthorizationTestData.test_acc_email)
    driver.find_element(*AuthLocators.password_input).send_keys(test_data.AuthorizationTestData.test_acc_password)
    driver.find_element(*AuthLocators.log_in_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((SuccessLoginLocators.account_name_after_authorization)))

    assert driver.find_element(*SuccessLoginLocators.account_name_after_authorization).text == 'User.'
    assert driver.find_element(*SuccessLoginLocators.profile_image_button).is_displayed()