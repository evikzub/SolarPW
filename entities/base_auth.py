from typing import Optional
from pydantic import BaseModel
from entities.test_users import test_users
from entities.base_entity import BaseEntity
from settings import ADMIN_LOGIN, ADMIN_PASSWORD

class BaseAuth(BaseModel):
    login: BaseEntity
    password: BaseEntity
    sugnup: BaseEntity
    remember: Optional[BaseEntity] = None

base_auth = {
    "login": {
        "locator": "input[id='data.email']",
        "value": None
    },
    "password": {
        "locator": "input[id='data.password']",
        "value": None
    }, 
    "sugnup": {
        "locator": "button[type='submit']",
    },
    "remember": {
        # "locator": "input[id='data.remember']",
        "locator": "input[type=checkbox]",
        "value": "True"
    }, 
}

def get_client_auth():
    client_auth = base_auth.copy()
    client_auth['login']['value'] = test_users.get_activated.login
    client_auth['password']['value'] = test_users.get_activated.password
    return client_auth

def get_admin_auth():
    admin_auth = base_auth.copy()
    admin_auth['login']['value'] = ADMIN_LOGIN
    admin_auth['password']['value'] = ADMIN_PASSWORD
    return admin_auth


client = BaseAuth.model_validate(get_client_auth())
admin = BaseAuth.model_validate(get_admin_auth())
