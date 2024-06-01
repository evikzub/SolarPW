from pydantic import BaseModel
from entities.test_users import test_users
from entities.base_entity import BaseEntity

class ClientAuth(BaseModel):
    login: BaseEntity
    password: BaseEntity
    sugnup: BaseEntity

client_auth = {
    "login": {
        "locator": "input[id='data.email']",
        "value": test_users.get_activated.login
    },
    "password": {
        "locator": "input[id='data.password']",
        "value": test_users.get_activated.password
    }, 
    "sugnup": {
        "locator": "button[type='submit']",
    }    
}

# client = ClientAuth.model_validate(client_auth)
