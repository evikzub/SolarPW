from playwright.sync_api import Page
from factory.checkbox import Checkbox
from factory.input import Input
from factory.button import Button
from pages.base import BasePage
from entities.base_auth import client, admin

CLIENT_LOGIN = "/customer/login"
ADMIN_LOGIN = "/admin/login"

CLIENT_MAIN = "/customer"
ADMIN_MAIN = "/admin"


class Login(BasePage):
    def __init__(self, page: Page, is_admin: bool = False) -> None:
        super().__init__(page)
        self.login = Input(page, admin.login if is_admin else client.login)
        self.password = Input(page, admin.password if is_admin else client.password)
        self.submit = Button(page, admin.sugnup if is_admin else client.sugnup)
        self.remeber = Checkbox(page, admin.remember if is_admin else client.remember)
        self.is_admin = is_admin

    def user_login(self):
        self.visit(ADMIN_LOGIN if self.is_admin else CLIENT_LOGIN)
        self.login.fill()
        self.password.fill()
        self.remeber.check()
        self.submit.click()
        self.check_URL(ADMIN_MAIN if self.is_admin else CLIENT_MAIN, "Wrong URL")
        # session_storage = self.page.evaluate("() => JSON.stringify(sessionStorage)")
        # print(session_storage)
        # self.page.pause()
