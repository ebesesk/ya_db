from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from database import get_db

from . import users_schema
from . import users_crud
from config import settings
from models import User
from ..login.login_router import get_current_user

router = APIRouter()

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: users_schema.UserCreate, 
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)
                ):
    user = users_crud.get_existing_user(db=db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='이미 존재하는 사용자입니다.')
    users_crud.create_user(db=db, user_create=_user_create)