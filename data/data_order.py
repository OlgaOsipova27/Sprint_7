from helpers.base import BaseMethod


def data_to_create_order():
    return [
        {
            "firstName": BaseMethod.generate_random_string(5),
            "lastName": BaseMethod.generate_random_string(10),
            "address": "Москва, ул. Ленина, 10",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2026-06-06",
            "comment": BaseMethod.generate_random_string(10),
            "color": ["BLACK"]
        },
        {
            "firstName": BaseMethod.generate_random_string(5),
            "lastName": BaseMethod.generate_random_string(10),
            "address": "Москва, ул. Пушкина, 15",
            "metroStation": 7,
            "phone": "+7 999 123 45 67",
            "rentTime": 3,
            "deliveryDate": "2026-06-07",
            "comment": BaseMethod.generate_random_string(10),
            "color": ["GREY"]
        },
        {
            "firstName": BaseMethod.generate_random_string(5),
            "lastName": BaseMethod.generate_random_string(10),
            "address": "Москва, пр. Мира, 20",
            "metroStation": 7,
            "phone": "+7 999 123 45 67",
            "rentTime": 3,
            "deliveryDate": "2026-06-07",
            "comment": BaseMethod.generate_random_string(10),
            "color": ["BLACK", "GREY"]
        },
        {
            "firstName": BaseMethod.generate_random_string(5),
            "lastName": BaseMethod.generate_random_string(10),
            "address": "Москва, ул. Тверская, 5",
            "metroStation": 7,
            "phone": "+7 999 123 45 67",
            "rentTime": 3,
            "deliveryDate": "2026-06-07",
            "comment": BaseMethod.generate_random_string(10),
            "color": []
        }
    ]
