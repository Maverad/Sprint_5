from conftest import driver
from locators.locators_success_login import SuccessLoginLocators 
from locators.locators_ad import AdLocators
import test_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestAd:

    def test_create_an_ad_with_autorization(self, driver_with_reg):
        driver_with_reg.find_element(*AdLocators.create_an_ad_button).click()
        WebDriverWait(driver_with_reg, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AdLocators.add_photo_button)))
        driver_with_reg.find_element(*AdLocators.ad_name).send_keys(test_data.AdData.name)
        driver_with_reg.find_element(*AdLocators.ad_dropdown_type_button).click()
        driver_with_reg.find_element(*AdLocators.ad_dropdown_type_choise_button).click()
        driver_with_reg.find_element(*AdLocators.ad_radio_button).click()
        driver_with_reg.find_element(*AdLocators.ad_dropdown_city_button).click()
        driver_with_reg.find_element(*AdLocators.ad_dropdown_city_choise_button).click()
        driver_with_reg.find_element(*AdLocators.ad_description).send_keys(test_data.AdData.description)
        driver_with_reg.find_element(*AdLocators.ad_price).send_keys(test_data.AdData.price)
        driver_with_reg.find_element(*AdLocators.ad_publish).click()
        element = WebDriverWait(driver_with_reg, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((SuccessLoginLocators.profile_image_button)))
        ActionChains(driver_with_reg).move_to_element(element).click().perform()
        WebDriverWait(driver_with_reg, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AdLocators.created_ad)))

        assert driver_with_reg.find_element(*AdLocators.created_ad).get_attribute('alt') == test_data.AdData.name

    def test_create_an_ad_with_no_autorization(self, driver):
        driver.find_element(*AdLocators.create_an_ad_button).click()
        WebDriverWait(driver, test_data.Timeouts.base_timeout).until(EC.visibility_of_element_located((AdLocators.log_in_modal_to_create_an_ad_header)))

        assert driver.find_element(*AdLocators.log_in_modal_to_create_an_ad_header).is_displayed()