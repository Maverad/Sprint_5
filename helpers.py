import datetime
import random

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

