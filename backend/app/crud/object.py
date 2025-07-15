from sqlalchemy.orm import Session
from backend.app.models.object import Object
from backend.app.schemas.object import *


def get_object(session: Session, id_object: int):
    return session.query(Object).filter(Object.id == id_object).first()


def get_objects(session: Session):
    return session.query(Object).all()


def create_object(session: Session, object: ObjectCreate):
    object_add = Object(object.name, object.id_campaign, object.bio, object.image_path)
    session.add(object_add)
    session.commit()
    session.refresh(object_add)
    return object_add