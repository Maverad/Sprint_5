import random 
import datetime

class Urls:
    main_url = "https://qa-desk.education-services.ru/"

class AuthorizationTestData:
    test_acc_email = "testik@mail.com"
    test_acc_password = "123"

class Timeouts:
    base_timeout = 3

class AdData:
    name = 'Продаётся книга "Мертвые души"'
    description = 'Книга хорошо сохранилась, в пользовании 1 месяц'
    price = 500

class ValidationData:
    wrong_email = 'wrongemail'

class GenerateData:

    @staticmethod
    def generate_email():
        domens = ['yandex.ru', 'mail.ru', 'gmail.com', 'rambler.ru', 'outlook.com', 'yahoo.com']
        email = ''
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in range(10):
            email += alphabet[random.randint(0, 25)].lower()
        return f'{email}@{domens[random.randint(0, 5)]}'
    
    @staticmethod
    def generate_password():
        password = ''
        now = datetime.datetime.now()
        for i in range(3):
            password += f'{now.second}{now.day}'
        return f'A{password}@z'
    