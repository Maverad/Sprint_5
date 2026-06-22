from locators.locators_authorization import AuthLocators
from locators.locators_success_login import SuccessLoginLocators
import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_log_out(driver_with_reg):
    driver_with_reg.find_element(*SuccessLoginLocators.log_out_button).click()
    WebDriverWait(driver_with_reg, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AuthLocators.log_in_and_registration_button)))

    assert driver_with_reg.find_element(*AuthLocators.log_in_and_registration_button).is_displayed()
    assert len(driver_with_reg.find_elements(*SuccessLoginLocators.profile_image_button)) == 0
    assert len(driver_with_reg.find_elements(*SuccessLoginLocators.account_name_after_authorization)) == 0
