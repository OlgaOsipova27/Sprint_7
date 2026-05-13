import pytest
import allure

from helpers.base import BaseMethod
from data.data_order import data_to_create_order

class TestCreateOrder:
    @allure.title('Создание заказа с разными цветами, и без них, успешно')
    @pytest.mark.parametrize("payload", data_to_create_order())
    def test_create_order(self, payload):
        response = BaseMethod.create_order(payload)
        track = response.json()["track"]
 
        try:
            assert response.status_code == 201
            assert "track" in response.json()
            assert response.json()["track"] is not None
        finally:
            BaseMethod.cancel_order(track)

class TestOrderList:


    @allure.title('Получение списка заказов успешно')
    def test_get_order_list(self):
        

        response = BaseMethod.get_order()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)



