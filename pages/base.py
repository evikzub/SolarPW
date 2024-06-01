import allure
from playwright.sync_api import Page, Response, expect
from settings import get_url

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def current_url(self) -> str: #возвращает урл
        return self.page.url

    def visit(self, uri: str) -> Response | None:
        url = get_url(uri)
        with allure.step(f'Opening the url "{url}"'):
            # return self.page.goto(url, wait_until='networkidle')
            return self.page.goto(url, wait_until='domcontentloaded')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')
        
    # def input(self, locator: str, data: str) -> None: #ввод в поле
    #     with allure.step(f'Input text: "{locator}" "{data}"'):
    #         self.page.locator(locator).fill(data)

    # def click(self, locator: str) -> None:
    #     with allure.step(f'Button click: "{locator}"'):
    #         # self.page.get_by_role("button", name=locator).click()
    #         self.page.click(locator)

    def check_URL(self, uri: str, msg: str) -> None:
        expect(self.page).to_have_url(get_url(uri), timeout=10000), msg

