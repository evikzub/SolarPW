from os import environ, path

BASE_URL = environ.get("BASE_URL")
assert BASE_URL, "BASE_URL is not set"

ADMIN_LOGIN = environ.get("ADMIN_LOGIN")
assert ADMIN_LOGIN, "ADMIN_LOGIN is not set"

ADMIN_PASSWORD = environ.get("ADMIN_PASSWORD")
assert ADMIN_PASSWORD, "ADMIN_PASSWORD is not set"

TEST_USERS = environ.get("TEST_USERS")
assert TEST_USERS, "TEST_USERS are not set"


def get_url(uri: str) -> str:
    return f"{BASE_URL}{uri}"


ADMIN_URL = get_url("/admin")


def get_header(session: str) -> dict:
    return {"cookie": f"residential_energy_partners_session={session}"}


ADMIN_SESSION_FILE = path.join(path.dirname(__file__), "data", "admin_session.txt")


def store_cookie(key: str):
    with open(ADMIN_SESSION_FILE, "w") as f:
        f.write(key)


def retrieve_cookie():
    if not path.exists(ADMIN_SESSION_FILE):
        return None
    with open(ADMIN_SESSION_FILE, "r") as f:
        return f.read()


def get_admin_session():
    return environ.get("ADMIN_SESSION")

def set_admin_session(session: str):
    environ["ADMIN_SESSION"] = session
