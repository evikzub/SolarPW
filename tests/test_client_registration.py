import pytest
from playwright.sync_api import Page
from pages.register import RegisterClient


@pytest.mark.smoke
class TestRegistration:
    def test_user_login(self, chromium_page: Page):
        rc = RegisterClient(chromium_page)
        rc.client_info()
        rc.client_tariff()
