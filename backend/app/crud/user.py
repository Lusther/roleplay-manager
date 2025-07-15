from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.schemas.user import *


def get_user(session: Session, id_user: int):
    return session.query(User).filter(User.id == id_user).first()


def get_users(session: Session):
    return session.query(User).all()


def create_user(session: Session, user: UserCreate):
    user_add = User(user.name, user.password, user.is_admin)
    session.add(user_add)
    session.commit()
    session.refresh(user_add)
    return user_add
