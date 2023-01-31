from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import users_schema
from models import User
# from .. login.login_router import pwd_context

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_existing_user(db: Session, user_create: users_schema.UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) | (User.email == user_create.email)
    ).first()

def create_user(db: Session, user_create: users_schema.UserCreate):
    db_user = User(username = user_create.username,
                   hashed_password = pwd_context.hash(user_create.password1),
                   email = user_create.email)
    db.add(db_user)
    db.commit()
    
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()