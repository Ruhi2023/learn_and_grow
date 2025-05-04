# this file will contain schemas all that will be used for api

from pydantic import BaseModel
from typing import List

class UserLoginIn(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True

class UserRegisterIn(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        orm_mode = True
class JwtTokenIn(BaseModel):
    token: str