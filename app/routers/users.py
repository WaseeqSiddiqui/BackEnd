from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import models,schemas,utils
from ..database import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/users",tags=["Users"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    hashed_password=utils.hash_password(user.password)
    user.password=hashed_password
    created_user=models.User(**user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user


@router.get("/{id}",response_model=schemas.UserOut)
def get_oneUser(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id: {id} does not exist")
    return user
      