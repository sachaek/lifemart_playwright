import logging
import pytest
from playwright.sync_api import Browser


@pytest.mark.smoke
@pytest.mark.skip
class TestMap:
    def test_incorrect_map_address(self, browser: Browser):
        logging.info("Проверяем корректность отображения информации о недоступном адресе для доставки")
        pass


    def test_input_address_search(self, browser):
        logging.info("Проверяем возможность выбор адреса для доставки через поиск")
        pass

    def test_input_address_in_map(self, browser):
        logging.info("Проверяем возможность выбора адреса для доставки через карту")
        pass