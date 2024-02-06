from typing import List
from pydantic import BaseModel

class UserPinData(BaseModel):
    seller_id: str
    pins: List[str]
