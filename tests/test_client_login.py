import pytest
from pages.login import Login
from playwright.sync_api import Page


@pytest.mark.smoke
class TestClientLogin:
    def test_user_login(self, default_page: Page):
        m = Login(default_page)
        m.user_login()
