import logging
import pytest
from playwright.sync_api import Browser
from data.constants import Constants


@pytest.mark.smoke
@pytest.mark.skip
class TestGeolocation:
    def test_geolocation(self, browser: Browser) -> None:
        logging.info("Проверяем, что сервер обработал данные по геолокации, и мы можем перейти в корзину")
        context_options = Constants.get_browser_context_options_geolocation()
        context = browser.new_context(**context_options)
        page = context.new_page()
        pass