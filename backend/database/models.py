from ast import Bytes
from encodings.punycode import T
from .database_main import Base
from sqlalchemy.types import TIMESTAMP, BINARY
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, Text
from sqlalchemy.sql.expression import text
# Tables i will need 
# a) users
# 
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,nullable=False)
    username = Column(String, unique=True)
    email = Column(String, unique=True,nullable= False)
    hashed_password = Column(Text,nullable=False)
    salt = Column(Text,nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    is_active = Column(Boolean, default=True)


# class User_Data(Base):
#     __tablename__ = "users_data"

#     id = Column(Integer, primary_key=True, index=True,nullable=False)
#     username = Column(String, unique=True)
#     # user_id = 

