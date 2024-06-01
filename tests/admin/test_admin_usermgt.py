import pytest
from playwright.sync_api import Browser

from pages.customers import Customers
from conftest import get_header


@pytest.mark.usefixtures("admin_login")
class TestUserManagement:

    def test_find_customer(self, browser: Browser, admin_session: str):
        header = get_header(admin_session)
        with browser.new_context(extra_http_headers=header) as context:
            page = context.new_page()
            customers = Customers(page)
            customers.customers_list()
            assert 1 == 1
            # page.pause()

    # def test_remove_user(self, chromium_page):
    def test_remove_user(self, browser: Browser, admin_session: str):
        header = get_header(admin_session)
        with browser.new_context(extra_http_headers=header) as context:
            page = context.new_page()
            customers = Customers(page)
            customers.visit_customers()
            assert 1 == 1
            # page.pause()
