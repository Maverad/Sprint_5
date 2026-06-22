from locators.locators_ad import AdLocators
import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create_an_ad_with_no_autorization(driver):
    driver.find_element(*AdLocators.create_an_ad_button).click()
    WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AdLocators.log_in_modal_to_create_an_ad_header)))

    assert driver.find_element(*AdLocators.log_in_modal_to_create_an_ad_header).text == 'Чтобы разместить объявление, авторизуйтесь'