import logging
import pytest
from playwright.sync_api import Page, Route, Request, expect, Browser, BrowserContext

from data.environment import AUTH_STATE
from helpers.auth import Auth


@pytest.mark.smoke
@pytest.mark.auth
class TestAuth:
    def test_try_auth(self, browser: Browser):
        context = browser.new_context(
            http_credentials={"username": "test", "password": "tabletable"}
        )
        page = context.new_page()
        auth = Auth(page)
        auth.open_main()
        auth.check_modal_is_this_your_city()
        auth.open_model_auth_window()
        auth.authorization_process()
        auth.check_auth()
        context.storage_state(path=AUTH_STATE)
        page.close()


def test_fixture_auth(context_auth_group: BrowserContext):
    page = context_auth_group.new_page()
    pass