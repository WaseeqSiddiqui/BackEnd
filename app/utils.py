from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def auth_password(user_password,hashed_password):
    return pwd_context.verify(user_password,hashed_password)
    