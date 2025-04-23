# this file will have all the api utils

import hashlib
import os
from re import A
import traceback
from dotenv import load_dotenv, find_dotenv
import jwt

from ..database.database_main import get_db
from ..database.models import User

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
    


class Auth_for_user:
    def __init__(self):
        self.file_haser = hashlib.sha256()

    def hash_pass_with_salt(self, password):
        """
        Generate a random salt and hash the password with it
        """
        salt = os.urandom(16)
        hashed_password =hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
        #  now hashed password is a hexadecimal
        # !! if i don't give hex here the password at later authentication will give problems
        salt = salt.hex()
        # and
        return salt, hashed_password

    def verify_password(self, password:str, salt:str, hashed_password:str):
        """
        Verify that the provided password matches the hashed_password in db
        """
        byte_salt = bytes.fromhex(salt)
        byte_hashed_password = bytes.fromhex(hashed_password) #hashed_password
        from hmac import compare_digest
        curr_un_verified_pass  = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), byte_salt, 100000)
        return compare_digest(curr_un_verified_pass,byte_hashed_password)

    def generate_jwt_token(self, data:dict, EXPIRE_MINUTES:int =60):
        JWT_SECRTEKEY, ALGO_JWT = Credentials_helper().jwt_cred()
        # * to_not_change_the data that comes in the function
        dat_to_encode = data.copy()
        dat_to_encode.update({"exp":EXPIRE_MINUTES})
        token = jwt.encode(dat_to_encode, JWT_SECRTEKEY, algorithm=ALGO_JWT)
        return token
    
    def verify_jwt_token(self, token:str):
        JWT_SECRTEKEY, ALGO_JWT = Credentials_helper().jwt_cred()
        try:
            payload = jwt.decode(token, JWT_SECRTEKEY, algorithms=[ALGO_JWT])
            return payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}
        except Exception as e:
            traceback.print_exc()

    def get_user_from_token(self, payload:dict):
        db = get_db()
        user_id = payload.get("user_id")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return {"error": "User not found"}
        return user




