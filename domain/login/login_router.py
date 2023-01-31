from datetime import timedelta, datetime

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status
from sqlalchemy.orm import Session

from database import get_db
from . import login_schema
from ..users import users_crud
from ..users.users_crud import pwd_context
from config import settings


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

@router.post("", response_model=login_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    user = users_crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, settings.SECRET_KEY, settings.ALGORITHM)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }

def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    # print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-AUTHENTICATE": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = user_crud.get_user(db, username=username)
        if user is None:
            raise credentials_exception
        return user