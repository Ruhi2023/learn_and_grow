import jwt

import datetime as dt
import hashlib
from math import exp
import os
from backend.utils.cred_utils import Credentials_helper

from backend.database.models import User
from backend.database.models import get_db
import traceback
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
        exp_at = dt.datetime.now(dt.UTC) + dt.timedelta(minutes=EXPIRE_MINUTES)
        dat_to_encode.update({"exp":exp_at})
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
            return {"error": str(e)}

    def get_user_from_token(self, payload:dict):
        db = get_db()
        user_id = payload.get("user_id")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return {"error": "User not found"}
        return user


