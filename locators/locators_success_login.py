from selenium.webdriver.common.by import By

class SuccessLoginLocators:
    account_name_after_authorization = (By.XPATH, ".//h3[text()='User.']")
    log_out_button = (By.XPATH, ".//button[text()='Выйти']")
    profile_image_button = (By.XPATH, ".//button[@class='circleSmall']")
    first_card_after_login = (By.XPATH, "(.//li[@class='places__item card'])[1]")

