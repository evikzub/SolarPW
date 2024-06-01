from enum import Enum
from typing import Optional
from pydantic import BaseModel
from settings import TEST_USERS

class UserType(str, Enum):
    activated = 'activated' # default for happy path
    new = 'new' # for creating new user


class UserEntity(BaseModel):
    login: str
    password: str
    user_type: UserType
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class TestUsers(BaseModel):
    __test__ = False # attribute in classes that pytest should ignore
    users: list[UserEntity]
    
    @property
    def get_new(self) -> UserEntity:
        return [user for user in self.users if user.user_type == UserType.new][0]
    
    @property
    def get_activated(self) -> UserEntity:
        user = [user for user in self.users if user.user_type == UserType.activated][0]
        user.first_name = "Jane"
        return user


# user = {
#     "login": "jd@mail.com",
#     "password": "12345678",
#     "user_type": "activated"
# }

# users = {
#     "users": [
#     {
#         "login": "jd@mail.com",
#         "password": "12345678",
#         "user_type": "activated"
#     },
#     {
#         "login": "new_user",
#         "password": "new_user",
#         "user_type": "new"
#     },   
# ]}

test_users = TestUsers.model_validate_json(TEST_USERS.replace("'", "\""))
# print(test_users.get_activated)
# print(str(users))

