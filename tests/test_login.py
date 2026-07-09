from locators.locators_authorization import AuthLocators
from locators.locators_success_login import SuccessLoginLocators
import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:

    def test_user_log_in(self, driver):
        driver.find_element(*AuthLocators.log_in_and_registration_button).click()
        WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.log_in_button)))
        driver.find_element(*AuthLocators.email_input).send_keys(test_data.AuthorizationTestData.test_acc_email)
        driver.find_element(*AuthLocators.password_input).send_keys(test_data.AuthorizationTestData.test_acc_password)
        driver.find_element(*AuthLocators.log_in_button).click()
        WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((SuccessLoginLocators.account_name_after_authorization)))

        assert driver.find_element(*SuccessLoginLocators.account_name_after_authorization).is_displayed()
        assert driver.find_element(*SuccessLoginLocators.profile_image_button).is_displayed()

    def test_user_log_out(self, driver_with_reg):
        driver_with_reg.find_element(*SuccessLoginLocators.log_out_button).click()
        WebDriverWait(driver_with_reg, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.log_in_and_registration_button)))

        assert driver_with_reg.find_element(*AuthLocators.log_in_and_registration_button).is_displayed()
        assert len(driver_with_reg.find_elements(*SuccessLoginLocators.profile_image_button)) == 0
        assert len(driver_with_reg.find_elements(*SuccessLoginLocators.account_name_after_authorization)) == 0

