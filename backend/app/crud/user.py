from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import *


def get_user(session: Session, id_user: int):
    return session.query(User).filter(User.id == id_user).first()


def get_users(session: Session):
    print("Toto2")
    return session.query(User).all()


def create_user(session: Session, user: UserCreate):
    user_add = User(
        name=user.name,
        password=user.password,
        is_admin=user.is_admin
    )
    session.add(user_add)
    session.commit()
    session.refresh(user_add)
    return user_add
