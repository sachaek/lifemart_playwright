import logging
import pytest
from playwright.sync_api import Browser, BrowserContext


@pytest.mark.regression
class TestOrder:
    def test_navigate_cart(self, context_auth_group: BrowserContext) -> None:
        logging.info("Добавляем товар и переходим в корзину без оформления заказа")
        pass

        
    def test_create_order(self, browser: Browser):
        logging.info("Обычное оформление заказа")
        pass
        