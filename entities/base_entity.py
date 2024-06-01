from typing import Optional
from pydantic import BaseModel

class BaseEntity(BaseModel):
    locator: str
    value: Optional[str] = None
    name: Optional[str] = None
