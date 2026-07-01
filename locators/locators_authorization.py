from selenium.webdriver.common.by import By

class AuthLocators:
    log_in_and_registration_button = (By.XPATH, ".//button[text()='Вход и регистрация']")
    email_input = (By.XPATH, ".//input[@name='email']")
    password_input = (By.XPATH, ".//input[@name='password']")
    log_in_button = (By.XPATH, ".//button[text()='Войти']")
    no_account_button = (By.XPATH, ".//button[text()='Нет аккаунта']")
    close_auth_form_button = (By.CLASS_NAME, "popUp_XBtn__uEWoB")
    password_eye_button = (By.CLASS_NAME, "eyeButton")
    submit_password = (By.XPATH, ".//input[@name='submitPassword']")
    create_account_button = (By.XPATH, ".//button[text()='Создать аккаунт']")
    account_already_exists_button = (By.XPATH, ".//button[text()='Уже есть аккаунт']")
    email_validation_error = (By.XPATH, ".//span[text()='Ошибка']")
    inputs_border = (By.XPATH, ".//div[@class='input_inputError__fLUP9']")

