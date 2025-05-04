# this file will have all the api utils

import datetime as dt
import hashlib
from math import exp
import os
from re import A
import traceback
from dotenv import load_dotenv, find_dotenv

from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class Credentials_helper:
    def __init__(self):
        pass
    def get_postgres_connection_string(self):
        host = os.getenv("POSTGRES_HOST")
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWD")
        database = os.getenv("POSTGRES_DB")
        port=os.getenv("POSTGRES_PORT")
        self.connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        print("I am connecting to: ",self.connection_string)
        return self.connection_string
    def jwt_cred(self):
        JWT_SECRTEKEY = os.getenv("JWT_SECR")
        ALGO_JWT = os.getenv("ALGO_JWT")
        return JWT_SECRTEKEY, ALGO_JWT
    



