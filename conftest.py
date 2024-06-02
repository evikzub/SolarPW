import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from pages.login import Login
from settings import (
    ADMIN_URL,
    get_header,
    store_cookie,
    retrieve_cookie,
    get_admin_session,
    set_admin_session,
)


# @pytest.fixture(scope='function')
@pytest.fixture(scope="class")
def browser() -> Browser:
    print(">> Starting browser")
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=True)
        yield chromium
        chromium.close()


@pytest.fixture(scope="function")
def default_page(browser: Browser) -> Page:
    print(">> Starting default page")
    with browser.new_page() as page:
        yield page


@pytest.fixture(scope="function")
def admin_page(browser: Browser) -> Page:
    print(">> Starting admin page")
    page = browser.new_page()
    page.set_extra_http_headers(get_header(get_admin_session()))
    yield page
    page.close()


@pytest.fixture(scope="class")
def admin_login(browser: Browser):
    print(">> Preparing cookie value")
    admin_session = get_admin_session()
    if not admin_session:
        # get cookie from the file
        session = retrieve_cookie()
        if session:
            with browser.new_context(extra_http_headers=get_header(session)) as context:
                page = context.new_page()
                # page.goto(ADMIN_URL, wait_until='networkidle')
                page.goto(ADMIN_URL)

                # Check if session is valid
                if page.url == ADMIN_URL:
                    set_admin_session(session)
                else:
                    m = Login(page, is_admin=True)
                    m.user_login()
                    for cookie in context.cookies():
                        if "residential_energy_partners_session" == cookie["name"]:
                            admin_session = cookie["value"]
                            set_admin_session(session)
                            store_cookie(admin_session)
                            break

        # generate new session if a value from the file is not valid
        # print(">>> Generate new admin session <<<")
        # with browser.new_context() as context:
        #     page = context.new_page()
        #     m = Login(page, is_admin=True)
        #     m.user_login()
        #     for cookie in context.cookies():
        #         if "residential_energy_partners_session" == cookie["name"]:
        #             admin_session = cookie["value"]
        #             os.environ["ADMIN_SESSION"] = admin_session
        #             store_cookie(admin_session)
        #             break


# @pytest.fixture(scope="function")
# def admin_session() -> str:
#     return get_admin_session()
