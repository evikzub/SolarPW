from os import environ, path, makedirs

BASE_URL = environ.get("BASE_URL")
assert BASE_URL, "BASE_URL is not set"

SMTP_URL = environ.get("SMTP_URL")
assert BASE_URL, "SMTP_URL is not set"

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


DATA_FILE = environ.get("DATA_FILE", path.join(path.dirname(__file__), "data"))
ADMIN_SESSION_FILE = path.join(DATA_FILE, "admin_session.txt")

def store_cookie(key: str):
    if not path.exists(ADMIN_SESSION_FILE):
        # Create the directory if it doesn't exist
        makedirs(path.dirname(ADMIN_SESSION_FILE), exist_ok=True)
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
