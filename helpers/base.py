import requests
import random
import string
import allure

from data.url import CREATE_CURIER_URL, LOGIN_CURIER_URL, CREATE_ORDER_URL, CANCEL_ORDER_URL


class BaseMethod:
    
    @staticmethod
    @allure.step('Генерация случайный строк')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    
    @staticmethod
    @allure.step('Генерация набора данных для создания курьера')
    def generate_courier_payload():
        return {
            "login": BaseMethod.generate_random_string(10),
            "password": BaseMethod.generate_random_string(10),
            "firstName": BaseMethod.generate_random_string(10)
        }
    
    
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(payload):
        return requests.post(CREATE_CURIER_URL, data=payload)

    
    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(payload):
        return requests.post(LOGIN_CURIER_URL, data=payload)
    

    
    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(f"{CREATE_CURIER_URL}/{courier_id}")

    
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(payload):
        return requests.post(CREATE_ORDER_URL, json=payload)

    
    @staticmethod
    @allure.step('Получение списка заказов')
    def get_order():
        return requests.get(CREATE_ORDER_URL)
    
    
    @staticmethod
    @allure.step('Отмена заказа')
    def cancel_order(track):
        return requests.put(CANCEL_ORDER_URL, data={"track": track}) 
    
