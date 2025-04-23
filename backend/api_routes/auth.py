from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from backend.utils.api_utils import Auth_for_user
from backend.api_routes.schemas import UserLoginIn, UserRegisterIn
from ..database.models import User
from ..database.database_main import get_db

auth_router = APIRouter(tags=["Authentications"])

@auth_router.post("/login")
def login(user_credientls: UserLoginIn, db : Session = Depends(get_db)):
    """
    First verify the jwt token"""
    user = db.query(User).filter(User.username == user_credientls.username).first()
    print(user)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    auth_obj = Auth_for_user()
    is_correct_user =auth_obj.verify_password(user_credientls.password, user.salt, user.hashed_password)
    if not is_correct_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid username or password")
    
    token = auth_obj.generate_jwt_token({"user_id": user.id})

    return {"Token": "sample_token"}  


@auth_router.post("/register")
def register(user_credientls: UserRegisterIn, db : Session = Depends(get_db)):
    auth_obj = Auth_for_user()
    salt, hashed_password = auth_obj.hash_pass_with_salt(user_credientls.password)
    new_user = User(username=user_credientls.username, email=user_credientls.email, hashed_password=hashed_password, salt=salt)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "Success"} # now the user will have to login






