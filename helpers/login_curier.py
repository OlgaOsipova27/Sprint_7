from helpers.base import BaseMethod
import allure

class LoginCurier:
    
    @staticmethod
    @allure.step('Регистрация курьера')
    def register_new_courier_payload():
        
        payload = BaseMethod.generate_courier_payload()
        BaseMethod.create_courier(payload)

        return payload
    
    
    @staticmethod
    @allure.step('Логин курьера')
    def login_with_payload():
        payload = LoginCurier.register_new_courier_payload()
        payload.pop("firstName")
 
        response = BaseMethod.login_courier(payload)
        return response
