from selenium.webdriver.common.by import By

class AdLocators:
    create_an_ad_button = (By.XPATH, ".//button[text()='Разместить объявление']")
    log_in_modal_to_create_an_ad_header = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    add_photo_button = (By.CLASS_NAME,'plusIcon')
    ad_name = (By.XPATH, ".//input[@name='name']")
    ad_description = (By.XPATH, ".//textarea[@name='description']")
    ad_price = (By.XPATH, ".//input[@name='price']")
    ad_radio_button = (By.XPATH, "(.//div[@class='radioUnput_inputRegular__FbVbr'])[1]")
    ad_dropdown_type_button = (By.XPATH, "(.//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[1]")
    ad_dropdown_type_choise_button = (By.XPATH, ".//span[text()='Книги']")
    ad_dropdown_city_button = (By.XPATH, "(.//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[2]")
    ad_dropdown_city_choise_button = (By.XPATH, ".//span[text()='Санкт-Петербург']")
    ad_publish = (By.XPATH, ".//button[text()='Опубликовать']")
    created_ad = (By.XPATH, ".//img[@class='picture']")