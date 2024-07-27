from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schemas,database,models
from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from .config import settings

Oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")


ALGORITHM=settings.algorithm
SECRET_KEY=settings.secret_key
TOKEN_EXPIRE_MINUTES=settings.access_token_expire_minutes

def create_token_access(data:dict):
    to_encode=data.copy()
    to_expire=datetime.utcnow()+timedelta(TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":to_expire})
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("users_id")
        if id==None:
            raise credentials_exception
        token_data=schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token:str=Depends(Oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception=HTTPException(status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate credentials",
                                        headers={"WWW-Authenticate":"Bearer"})
    token=verify_token(token,credentials_exception)
    user=db.query(models.User).filter(models.User.id==token.id).first()
    return user
    
        