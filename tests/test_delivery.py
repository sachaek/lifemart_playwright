import logging
import pytest
from playwright.sync_api import Browser

from data.constants import Constants
from pages.main_delivery import Delivery


@pytest.mark.smoke
class TestDelivery:
    # @pytest.mark.debug
    def test_delivery_open(self, browser: Browser):
        logging.info("Открываем модалку доставки. Тип заказа Зал")
        context_options = Constants.get_browser_context_options_geolocation()
        context = browser.new_context(**context_options)
        page = browser.new_page(http_credentials={"username": "test", "password": "tabletable"})
        delivery_modal = Delivery(page)
        delivery_modal.open_main_page()
        delivery_modal.modal_to_select_address()
        delivery_modal.confirm_address()

    def test_selforder_open(self, browser):
        logging.info("Открываем модалку доставки. Тип заказа самовывоз")
        pass
