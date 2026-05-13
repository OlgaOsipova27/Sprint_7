import allure
from helpers.base import BaseMethod



class TestCreateCourier:
 
    def setup_method(self):
        self.payload = None
        self.courier_id = None
 
    def teardown_method(self):
        if self.courier_id is not None:
            BaseMethod.delete_courier(self.courier_id)
 
    
    @allure.title('Создание нового курьера с полным набором данных успешно')
    def test_create_new_courier_with_all_data(self):
        self.payload = BaseMethod.generate_courier_payload()
        response = BaseMethod.create_courier(self.payload)
 
        login_response = BaseMethod.login_courier(self.payload)
        if login_response.status_code == 200:
            self.courier_id = login_response.json()["id"]
 
        assert response.status_code == 201
        assert response.json() == {"ok": True}
 
    @allure.title('Создание нового курьера с данными полностью дублирующими уже созданного курьера выдает ошибку')
    def test_create_double_courier(self):
        self.payload = BaseMethod.generate_courier_payload()
 
        response1 = BaseMethod.create_courier(self.payload)
        response2 = BaseMethod.create_courier(self.payload)
 
        login_response = BaseMethod.login_courier(self.payload)
        if login_response.status_code == 200:
            self.courier_id = login_response.json()["id"]
 
        assert response1.status_code == 201
        assert response1.json() == {"ok": True}
        assert response2.status_code == 409
        assert response2.json()["message"] == "Этот логин уже используется"
 
    @allure.title('Создание нового курьера с login уже зарегестрированного курьера выдает ошибку')
    def test_create_courier_with_registered_login(self):
        self.payload = BaseMethod.generate_courier_payload()
        old_login = self.payload["login"]
 
        response1 = BaseMethod.create_courier(self.payload)
 
        login_response = BaseMethod.login_courier(self.payload)
        if login_response.status_code == 200:
            self.courier_id = login_response.json()["id"]
 
        payload2 = BaseMethod.generate_courier_payload()
        payload2["login"] = old_login
        response2 = BaseMethod.create_courier(payload2)
 
        assert response1.status_code == 201
        assert response1.json() == {"ok": True}
        assert response2.status_code == 409
        assert response2.json()["message"] == "Этот логин уже используется"


    @allure.title('Создание нового курьера без пароля выдает ошибку')
    def test_create_courier_without_password(self):
        payload = BaseMethod.generate_courier_payload()
        payload.pop("password")
 
        response = BaseMethod.create_courier(payload)
 
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
 
    @allure.title('Создание нового курьера без логина выдает ошибку')
    def test_create_courier_without_login(self):
        payload = BaseMethod.generate_courier_payload()
        payload.pop("login")
 
        response = BaseMethod.create_courier(payload)
 
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


class TestLoginCourier:

    def setup_method(self):
        self.payload = BaseMethod.generate_courier_payload()
        BaseMethod.create_courier(self.payload)

        login_response = BaseMethod.login_courier(self.payload)
        self.courier_id = None

        if login_response.status_code == 200 and "id" in login_response.json():
            self.courier_id = login_response.json()["id"]

    def teardown_method(self):
        if self.courier_id is not None:
            BaseMethod.delete_courier(self.courier_id)

    @allure.title('Авторизация курьера с корректными данными успешна')
    def test_courier_can_authorize(self):
        response = BaseMethod.login_courier(self.payload)

        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] is not None

    @allure.title('Авторизация без логина выдает ошибку')
    def test_courier_authorization_without_login_returns_error(self):
        payload = {
            "password": self.payload["password"]
            }

        response = BaseMethod.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Авторизация без пароля выдает ошибку')
    def test_courier_authorization_without_password_returns_error(self):
        payload = {
            "login": self.payload["login"]
        }

        response = BaseMethod.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Авторизация с незарегестрированным логином выдает ошибку')
    def test_courier_authorization_with_invalid_login_returns_error(self):
        
        invalid_payload = {
            "login": "wrong_login",
            "password": self.payload["password"]
        }

        response = BaseMethod.login_courier(invalid_payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Авторизация с некорректным паролем выдает ошибку')
    def test_courier_authorization_with_invalid_password_returns_error(self):
        invalid_payload = {
            "login": self.payload["login"],
            "password": "wrong_password"
        }

        response = BaseMethod.login_courier(invalid_payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Авторизация с несуществующими логин-пароль выдает ошибку')
    def test_nonexistent_courier_authorization_returns_error(self):
        payload = {
            "login": "testpracticum",
            "password": "passwordtest"
        }

        response = BaseMethod.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
