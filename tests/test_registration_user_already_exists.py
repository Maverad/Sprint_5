from locators.locators_authorization import AuthLocators
import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_user_already_exists(driver):
    driver.find_element(*AuthLocators.log_in_and_registration_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.no_account_button))).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located(AuthLocators.create_account_button))
    driver.find_element(*AuthLocators.email_input).send_keys(test_data.AuthorizationTestData.test_acc_email)
    driver.find_element(*AuthLocators.password_input).send_keys(test_data.AuthorizationTestData.test_acc_password)
    driver.find_element(*AuthLocators.submit_password).send_keys(test_data.AuthorizationTestData.test_acc_password)
    driver.find_element(*AuthLocators.create_account_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.email_validation_error)))
    borders_color = driver.find_elements(*AuthLocators.inputs_border)

    assert driver.find_element(*AuthLocators.email_validation_error).text == 'Ошибка'
    for i in borders_color:
        border_value = i.value_of_css_property('border')
        assert 'rgb(255, 105, 114)' in border_value