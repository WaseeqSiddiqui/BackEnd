from fastapi import status,HTTPException,Response,APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(tags=["Authentication"])

@router.post("/login",response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    owner=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not owner:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid user credentials")
    if not utils.auth_password(user_credentials.password,owner.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid user credentials")
    token=oauth2.create_token_access({"users_id":owner.id})
    return {"access_token":token,"token_type":"bearer"}