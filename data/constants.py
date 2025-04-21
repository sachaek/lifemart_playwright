import os
from data.environment import host


class Constants:
    login = '9999999999'
    password = '5917'
    address_delivery = 'Екатеринбург, Серов, улица Ленина , 40'
    address_hall = 'Хохрякова, 74'
    address_hall_header = 'Екатеринбург, Хохрякова , 74'
    address_hall_header_geolocation = 'Екатеринбург, улица Хохрякова , 74'
    email = 'test@mail.com'
    input_test_address = "Серов, улица Ленина, 165"
    expected_text_in_falling_list_test = "улица Ленина , 165 Серов"
    expected_text_in_header_test = "Екатеринбург, Серов, улица Ленина, 165"
    base_url_api = f"{host.get_base_url_api()}api/"
    latitude = 56.82643329698711
    longitude = 60.59467150233496

    @staticmethod
    def get_browser_context_options_geolocation() -> dict:
        """
        Функция возвращает словарь, который можно передать в контекст браузера для установки данных геолокации
        """
        return {
            "http_credentials": {"username": "test", "password": "tabletable"},
            "geolocation": {"latitude": Constants.latitude, "longitude": Constants.longitude},
            "permissions": ["geolocation"],
            "locale": "ru-RU",
            "timezone_id": "Asia/Yekaterinburg"
        }