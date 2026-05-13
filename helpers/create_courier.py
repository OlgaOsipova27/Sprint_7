from helpers.base import BaseMethod
import allure

class RegistrationNewCourier:
    
    @staticmethod
    @allure.step('Регистрация нового курьера')
    def register_new_courier():
        payload = BaseMethod.generate_courier_payload()
        response = BaseMethod.create_courier(payload)
        return response

