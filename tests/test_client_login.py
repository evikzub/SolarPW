import pytest
from pages.login import Login
from playwright.sync_api import Page


@pytest.mark.smoke
class TestClientLogin:
    def test_user_login(self, chromium_page: Page):
        m = Login(chromium_page)
        m.user_login()
