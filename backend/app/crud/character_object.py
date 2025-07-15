from sqlalchemy.orm import Session
from backend.app.models.character_object import CharacterObject
from backend.app.models.character import Character
from backend.app.models.object import Object
from backend.app.schemas.character_object import *


def get_character_object(session: Session, id_character: int, id_object: int):
    return session.query(CharacterObject).filter(Character.id == id_character, Object.id == id_object).first()


def get_objects_of_character(session: Session, id_character: int):
    return session.query(CharacterObject).filter(Character.id == id_character).all()


def get_characters_for_object(session: Session, id_object: int):
    return session.query(CharacterObject).filter(Object.id == id_object).all()


def create_character_object(session: Session, character_object: CharacterObjectCreate):
    character_object_add = CharacterObject(character_object.id_character, character_object.id_object, character_object.quantity)
    session.add(character_object_add)
    session.commit()
    session.refresh(character_object_add)
    return character_object_add
