from sqlalchemy.orm import Session
from app.models.object import Object
from app.schemas.object import *


def get_object(session: Session, id_object: int):
    return session.query(Object).filter(Object.id == id_object).first()


def get_objects(session: Session):
    return session.query(Object).all()


def create_object(session: Session, object: ObjectCreate):
    object_add = Object(
        name=object.name,
        id_campaign=object.id_campaign,
        bio=object.bio,
        image_path=object.image_path
    )
    session.add(object_add)
    session.commit()
    session.refresh(object_add)
    return object_add