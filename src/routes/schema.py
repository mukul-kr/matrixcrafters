from typing import List
from pydantic import BaseModel

class UserPinData(BaseModel):
    seller_id: str
    pins: List[int]

class UpdateUserPinData(BaseModel): 
    seller_id: str
    old_pin: int
    new_pin: int

class DeleteUserPinData(BaseModel):
    seller_id: str
    pin: int