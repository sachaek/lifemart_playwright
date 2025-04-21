import logging
import pytest


@pytest.mark.regression
@pytest.mark.skip
class TestAuthCart:
    def test_auth_cart(self, browser):
        logging.info("Авторизуемся в корзине и оформляем заказ")
        pass
